from django import forms
from .widgets import CustomClearableFileInput
from django.forms import inlineformset_factory
from .models import Product, Category, Review, ProductImage


class ProductImageForm(forms.ModelForm):
    """
    Form for product images
    """
    class Meta:
        model = ProductImage
        fields = ("images",)


class ProductForm(forms.ModelForm):
    """
    Form for product details
    """
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with additional
        choices for the 'category' field
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"

        self.fields["image"].help_text = (
            "Best image resolution is 380x380 and .webp format"
        )  # Add help_text to the 'image' field


# Define a formset for managing additional
# images associated with a product. This formset
# uses ProductImageForm as the form class.
ImageFormSet = inlineformset_factory(
    Product,
    ProductImage,
    form=ProductImageForm,
    fields=("images",),
    extra=1,
    can_delete=True,
)


class ReviewForm(forms.ModelForm):
    """
    Form for product reviews
    """
    class Meta:
        model = Review
        fields = ("text", "rating")

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with custom attributes
        based on whether the user has bought the product
        """
        super().__init__(*args, **kwargs)

        has_bought = self.initial.get("has_bought", False)

        if has_bought:
            self.fields["text"].widget.attrs["placeholder"] = "Your review..."
            self.fields["text"].widget.attrs["rows"] = 3
        else:
            self.fields["text"].widget.attrs["placeholder"] = ""
            self.fields["text"].widget.attrs["rows"] = 3
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = (
                "border-black rounded-0 profile-form-input"
            )
            field.label = False  # This removes the label from the form field

    def clean(self):
        """
        Validate the form data, checking if
        required fields are present
        """
        cleaned_data = super().clean()
        has_bought = cleaned_data.get(
            "has_bought", False
        )  # Default to False if not present
        text = cleaned_data.get("text", "")
        rating = cleaned_data.get("rating", "")

        if has_bought and not text:
            self.add_error("text", "This field is required.")
        if has_bought and not rating:
            self.add_error("rating", "This field is required.")
        return cleaned_data
