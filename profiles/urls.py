from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path(
        "order_history/<order_number>",
        views.order_history,
        name="order_history",
    ),
    path("profile_update/", views.profile_update, name="profile_update"),
    path(
        "profile_agreement/", views.profile_agreement, name="profile_agreement"
    ),
    path(
        "profile_delete/<int:pk>/", views.profile_delete, name="profile_delete"
    ),
]
