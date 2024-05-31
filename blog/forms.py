from django.utils.text import slugify
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post
from products.models import Category


class PostForm(forms.ModelForm):
    """
    PostForm for blog posting
    """
    class Meta:
        """
        Form fields
        """

        model = Post
        fields = [
            "title",
            "featured_image",
            "excerpt",
            "content",
        ]
        widgets = {
            "content": SummernoteWidget(attrs={"class": "form-control"}),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Max 50 characters",
                }
            ),
            "excerpt": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Max 75 characters",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"

    def form_valid(self, form):
        """
        Custom logic to handle form validation when creating a new blog post
        """
        form.instance.author_id = self.request.user.pk
        form.instance.slug = slugify(form.instance.title)

        return super().form_valid(form)
