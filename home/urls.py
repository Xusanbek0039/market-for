from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('company/', views.company, name='company'),
    path('partners/', views.partners, name='partners'),
    path('payments/', views.payments, name='payments'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('unsubscribe/<str:email>/', views.unsubscribe, name='unsubscribe'),
    path("newsletter", views.newsletter, name="newsletter"),
    path('contact-form/', views.contact_form, name='contact_form'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('return-policy/', views.return_policy, name='return_policy'),
    path('shipping-policy/', views.shipping_policy, name='shipping_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('warranty-policy/', views.warranty_policy, name='warranty_policy'),
]
