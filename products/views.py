from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.db.models import Avg, Q  # This is for searching queries
from django.db.models.functions import Lower
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required, user_passes_test
from .utils import calculate_rating_and_count
from .models import Product, Category, Review, ProductImage
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from .forms import ProductForm, ReviewForm, ImageFormSet


def all_products(request):
    """
    A view to show all products, including sorting
    and search queries
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        # Check and apply sorting parameters
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey

            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if sortkey == "rating":
                if "direction" in request.GET:
                    direction = request.GET["direction"]
                    if direction == "desc":
                        # Annotate (create a new) field 'average_rating' in
                        # the queryset for Product objects
                        # Avg aggregation function to calculate the average
                        # rating from related Review objects
                        # The 'review__rating' lookup is the relationship
                        # between Product and Review models by ForeignKey.
                        # Order the queryset in descending order based on the
                        # calculated 'average_rating'
                        products = products.annotate(
                            average_rating=Avg("review__rating")
                        ).order_by("-average_rating")
                    else:
                        products = products.annotate(
                            average_rating=Avg("review__rating")
                        ).order_by("average_rating")
            else:
                if "direction" in request.GET:
                    direction = request.GET["direction"]
                    if direction == "desc":
                        sortkey = f"-{sortkey}"
                products = products.order_by(sortkey)
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if "deal" in request.GET and request.GET["deal"] == "true":
            products = products.filter(deal=True)
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("products"))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    # Create a string representation of the current sorting for display
    current_sorting = f"{sort}_{direction}"

    # Calculate and attach ratings and counts to each product
    for product in products:
        rating_and_count = calculate_rating_and_count(product)
        product.average_rating = rating_and_count["average_rating"]
        product.review_count = rating_and_count["review_count"]
    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """
    Display the details of a specific product,
    including its reviews and rating form
    """
    product = get_object_or_404(Product, pk=product_id)
    images = ProductImage.objects.filter(product__id=product_id)

    for image in images:
        print(f"Image URL for {product.name}: {image.images.url}")
    if request.method == "POST" and request.user.is_authenticated:
        has_bought_product = has_bought(request.user, product)

        try:
            reviewed = Review.objects.get(
                user__id=request.user.id, product__id=product_id
            )
            review_form = ReviewForm(request.POST, instance=reviewed)
            review_form.save()
            messages.warning(
                request,
                "Only one review per customer! Your review has been updated!",
            )
            return redirect("product_detail", product_id=product_id)
        except Review.DoesNotExist:
            review_form = ReviewForm(request.POST)

            if review_form.is_valid():
                if has_bought_product:
                    review = review_form.save(commit=False)
                    review.user = request.user
                    review.product = product
                    review.save()
                    messages.success(request, "Review has been submitted")
                    return redirect("product_detail", product_id=product_id)
                else:
                    messages.error(
                        request,
                        "You can only write a review "
                        "for products you have bought.",
                    )
            else:
                messages.error(
                    request,
                    "Invalid form submission. Please check your inputs.",
                )
    else:
        has_bought_product = (
            has_bought(request.user, product)
            if request.user.is_authenticated
            else False
        )
        review_form = ReviewForm(
            initial={
                "has_bought": (
                    request.user.is_authenticated and has_bought_product
                )
            }
        )
    reviews = product.review_set.all().order_by("-created_at")

    # from utils.py - calculate_rating_and_count
    rating_and_count = calculate_rating_and_count(product)

    context = {
        "product": product,
        "reviews": reviews,
        "review_form": review_form,
        "average_rating": rating_and_count["average_rating"],
        "star_percentages": rating_and_count["star_percentages"],
        "review_count": rating_and_count["review_count"],
        "has_bought": has_bought_product,
        "images": images,
        "one_star_count": rating_and_count["one_star_count"],
        "two_star_count": rating_and_count["two_star_count"],
        "three_star_count": rating_and_count["three_star_count"],
        "four_star_count": rating_and_count["four_star_count"],
        "five_star_count": rating_and_count["five_star_count"],
        "five_star_percentage": rating_and_count["five_star_percentage"],
        "four_star_percentage": rating_and_count["four_star_percentage"],
        "three_star_percentage": rating_and_count["three_star_percentage"],
        "two_star_percentage": rating_and_count["two_star_percentage"],
        "one_star_percentage": rating_and_count["one_star_percentage"],
    }
    return render(request, "products/product_detail.html", context)


def has_bought(user, product):
    """
    Check if specified user
    has bought the given product
    """
    order_line_items = OrderLineItem.objects.filter(
        order__user_profile__user=user, product=product
    )
    return (
        order_line_items.exists()
    )  # Check if at least one order line item exists


@user_passes_test(lambda u: u.is_superuser, login_url="home")
@login_required
def delete_review(request, review_id):
    """
    Delete a review if the user is a superuser
    """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, "Review is deleted!")
    return redirect("product_detail", product_id=review.product.id)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owner can do that.")
        return redirect(reverse("home"))
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm()
    template = "products/add_product.html"

    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owner can do that.")
        return redirect(reverse("home"))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")
    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store with
    confirmation step
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owner can do that.")
        return redirect(reverse("home"))
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product.delete()
        messages.success(request, f"{product.name} has been deleted")
        return redirect(reverse("products"))
    template = "products/delete_product.html"

    context = {"product": product}
    return render(request, template, context)
