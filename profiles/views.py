from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UpdatePersonalInfoForm
from .models import UserProfile
from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile with
    order history and defualt shipping form
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request, "Update failed. Please ensure the form is valid."
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "on_profile_page": (
            True
        ),  # Boolean value for only display succes msg
    }
    return render(request, template, context)


@login_required
def profile_update(request):
    """
    View for updating the user's
    personal information
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        personal_form = UpdatePersonalInfoForm(request.POST, request.FILES, instance=profile)

        if form.is_valid() and personal_form.is_valid():
            form.save()
            personal_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        form = UserProfileForm(instance=profile)
        personal_form = UpdatePersonalInfoForm(instance=profile)

    context = {
        "personal_form": personal_form,
        "orders": orders,
        "form": form,
    }
    return render(request, "profiles/profile_update.html", context)


@login_required
def profile_delete(request, pk):
    """
    Handles the deletion of a user profile
    and related objects
    """
    user = get_object_or_404(User, id=pk)
    logout(request)
    user.delete()
    messages.warning(request, "Your account has been deleted")
    return redirect("home")


def order_history(request, order_number):
    """
    Display users order history
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )
    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }
    return render(request, template, context)


def profile_agreement(request):
    """
    Render the profil_agreement.html template
    """
    return render(request, "profiles/profile_agreement.html")
