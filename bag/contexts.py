from django.conf import settings
from decimal import Decimal
from products.models import Product


def bag_contents(request):
    """
    Calculate the contents and total value
    of the shopping bag
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    # Create a copy of the bag
    bag_copy = bag.copy()

    # Iterate over the original bag while modifying the copy
    for item_id, quantity in bag_copy.items():
        try:
            product = Product.objects.get(pk=item_id)
            total += quantity * product.price
            product_count += quantity
            bag_items.append(
                {
                    "item_id": item_id,
                    "quantity": quantity,
                    "product": product,
                }
            )
        except Product.DoesNotExist:
            print(
                f"Product with ID {item_id} not found. Removing from the bag."
            )
            # Remove the non-existent product from the bag
            del bag[item_id]
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PRECENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    grand_total = delivery + total

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }
    return context
