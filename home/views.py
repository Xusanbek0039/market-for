from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ContactForm, NewsletterForm
from .models import SubscribedUsers
from blog.models import Post
from products.models import Product


def index(request):
    """
    View to return the index page
    """
    posts = Post.objects.all()
    # Fetch the three newest posts for display
    latest_posts = Post.objects.order_by("-created_on")[:3]
    new_arrivals = Product.objects.order_by("-created_at")

    context = {
        "posts": latest_posts,
        "products": new_arrivals,
    }
    return render(request, "home/index.html", context)


def contact(request):
    """
    Render contact.html view
    """
    return render(request, "home/support/contact.html")


def company(request):
    """
    Render company.html view
    """
    return render(request, "home/information/company.html")


def contact_form(request):
    """
    Contact form view
    """
    template = "home/support/contact_form.html"
    form = ContactForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = ContactForm(request.POST, request.FILES)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.user = request.user
                contact.save()
                messages.success(request, "Successfully form submission!")
                return redirect(reverse("contact_form"))
            else:
                messages.error(
                    request,
                    "Failed to submit the form. "
                    "Please ensure the form is valid.",
                )
        else:
            messages.warning(request, "You need to be logged in.")
    context = {
        "form": form,
    }
    return render(request, template, context)


def partners(request):
    """
    Render partners.html view
    """
    return render(request, "home/information/partners.html")


def payments(request):
    """
    Render payments.html view
    """
    return render(request, "home/information/payments.html")


def privacy_policy(request):
    """
    Render privacy_policy.html view
    """
    return render(request, "home/information/privacy_policy.html")


def return_policy(request):
    """
    Render return_policy.html view
    """
    return render(request, "home/information/return_policy.html")


def shipping_policy(request):
    """
    Render shipping_policy.html view
    """
    return render(request, "home/information/shipping_policy.html")


def terms_of_service(request):
    """
    Render terms_of_service.html view
    """
    return render(request, "home/information/terms_of_service.html")


def warranty_policy(request):
    """
    Render warranty_policy.html view
    """
    return render(request, "home/information/warranty_policy.html")


@user_passes_test(lambda user: user.is_superuser)
def newsletter(request):
    """
    Send newsletter to subscribers with
    individual unsubscribe links
    """
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("subject")
            receivers = form.cleaned_data.get("receivers").split(",")
            email_message = form.cleaned_data.get("message")

            # Iterate through subscribers and include
            # unsubscribe links with personally email
            for subscriber in SubscribedUsers.objects.all():
                unsubscribe_link = (
                    f"http://127.0.0.1:8000/unsubscribe/{subscriber.email}/"
                )
                email_message_with_unsubscribe = (
                    f"{email_message}\n\nUnsubscribe link: {unsubscribe_link}"
                )

                # Create the EmailMessage object
                mail = EmailMessage(
                    subject,
                    email_message_with_unsubscribe,
                    f"EasyKeyboardMaker <{request.user.email}>",
                    to=[subscriber.email],
                )
                mail.content_subtype = "html"

                # Send the email to the current subscriber
                if mail.send():
                    messages.success(
                        request,
                        f"Email sent successfully to {subscriber.email}",
                    )
                else:
                    messages.error(
                        request,
                        f"There was an error "
                        f"sending email to {subscriber.email}",
                    )
            return redirect("/")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect("/")
    form = NewsletterForm()
    form.fields["receivers"].initial = ",".join(
        [active.email for active in SubscribedUsers.objects.all()]
    )
    return render(
        request=request,
        template_name="home/newsletter.html",
        context={"form": form},
    )


def subscribe(request):
    """
    Handle newsletter subscription
    """
    if request.method == "POST":
        email = request.POST.get("email", None)

        if not email:
            messages.error(
                request,
                "You must type a legitimate email "
                "address to subscribe to the newsletter",
            )
            return redirect("/")
        if User.objects.filter(email=email).exists():
            messages.error(
                request,
                f"A user with the email {email} already exists. "
                f"Please log in to subscribe or unsubscribe.",
            )
            return redirect(request.META.get("HTTP_REFERER", "/"))
        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(
                request, f"{email} email address is already a subscriber."
            )
            return redirect(request.META.get("HTTP_REFERER", "/"))
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")
        subscribe_model_instance = SubscribedUsers(email=email)
        subscribe_model_instance.save()

        # Send thank-you email
        subscribe_model_instance.send_thank_you_email()

        messages.success(
            request,
            f"{email} email was successfully subscribed to our newsletter!",
        )
        return redirect(request.META.get("HTTP_REFERER", "/"))
    return HttpResponse("Invalid request")


def unsubscribe(request, email):
    """
    Unsubscribe the user associated with
    the provided email address
    """
    try:
        subscriber = SubscribedUsers.objects.get(email=email)
        unsubscribed = subscriber.unsubscribe()
        if unsubscribed:
            messages.success(
                request, "You have been unsubscribed successfully."
            )
            return HttpResponse(
                "You have been unsubscribed successfully. If you wish "
                "to subscribe again, please do so on the home page."
            )
        else:
            return HttpResponse(
                "Invalid unsubscribe link or you are already unsubscribed."
            )
    except SubscribedUsers.DoesNotExist:
        return HttpResponse(
            "Invalid unsubscribe link or you are already unsubscribed."
        )
