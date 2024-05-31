from django.db import models
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class contact_form(models.Model):
    """
    Model for contact form
    """
    CONTACT_CHOICES = [
        ("order", "Order Tracking"),
        ("order", "Order Issue"),
        ("general", "General Query"),
        ("complaint", "Complaint"),
        ("return", "Return Request"),
    ]
    reason = models.CharField(max_length=15, choices=CONTACT_CHOICES)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=700)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact Form"


class SubscribedUsers(models.Model):
    """
    Model for storing subscribed users information
    """
    email = models.EmailField(unique=True, max_length=45)
    created_date = models.DateTimeField("Date created", default=timezone.now)
    subscribed = models.BooleanField(default=True)

    def send_thank_you_email(self):
        print(f"Sending thank you email to {self.email}")
        subject = "Thank You for Subscribing!"
        unsubscribe_link = f"http://127.0.0.1:8000/unsubscribe/{self.email}/"
        message = render_to_string(
            "home/email_templates/thank_you_email.html", {"user": self}
        )
        email = EmailMessage(subject, message, to=[self.email])
        email.content_subtype = "html"
        email.send()

    def unsubscribe(self):
        try:
            # Attempt to get the associated SubscribedUsers instance
            subscriber = SubscribedUsers.objects.get(
                email=self.email, subscribed=True
            )
            # Set subscribed to False and save
            subscriber.subscribed = False
            subscriber.save()

            # Delete the instance
            subscriber.delete()

            # Indicate successful unsubscribe
            return True
        except SubscribedUsers.DoesNotExist:
            return False

    def __str__(self):
        return self.email
