from django.contrib import admin
from .models import contact_form, SubscribedUsers


class ContactFormAdmin(admin.ModelAdmin):
    """
    Admin class for managing ContactForm instances
    """
    list_display = (
        'email',
        'subject',
        'reason',
        'submission_date',
    )


class SubscribedAdmin(admin.ModelAdmin):
    """
    Admin class for managing SubscribedUsers instances
    """
    list_display = (
        'email',
        'created_date',
    )


admin.site.register(contact_form, ContactFormAdmin)
admin.site.register(SubscribedUsers, SubscribedAdmin)
