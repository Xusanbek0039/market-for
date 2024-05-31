from django import forms
from .models import contact_form


class ContactForm(forms.ModelForm):
    """
    Form for composing and sending newsletters
    """
    class Meta:
        model = contact_form
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholder and classes, remove labels and set focus
        on first name field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
            'reason': 'Reason for contact',
        }

        self.fields['email'].widget.attrs['autofocus'] = True


class NewsletterForm(forms.Form):
    """
    Form for composing and sending newsletters
    """
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(label="Email content")
