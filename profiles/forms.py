from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    User form for updating the shipping
    information
    """
    class Meta:
        model = UserProfile
        exclude = (
            "user",
            "bio",
            "first_name",
            "last_name",
            "profile_picture",
            "country",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Locality",
        }
        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs[
                "class"
            ] = "border-black rounded-0 profile-form-input"
            self.fields[field].label = False


class UpdatePersonalInfoForm(forms.ModelForm):
    """
    User form for updating personal
    information for user page
    """
    class Meta:
        model = UserProfile
        fields = (
            "first_name",
            "last_name",
            "bio",
            "profile_picture",
            "country",
        )

        widgets = {
                'bio': forms.Textarea(attrs={'style': 'height: 55px;'}),  # Adjust the height as needed
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "bio": "Something about Yourself",
            "country": "In which Country do you live?",
        }

        for field_name, placeholder in placeholders.items():
            self.fields[field_name].widget.attrs["placeholder"] = placeholder
        
        self.fields["profile_picture"].help_text = "Best image resolution is 512x512 and .webp format"
