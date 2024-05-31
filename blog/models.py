from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Database model for posts
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(max_length=75, blank=True)
    content = models.TextField(max_length=3000, blank=True)
    featured_image = models.ImageField(
        blank=True, upload_to="userprofile/", default="images/no-product-img.png"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        """
        Set the order of posts by date descending
        """
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a unique slug based on the title and timestamp
            base_slug = slugify(self.title)
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
            unique_slug = f"{base_slug}-{timestamp}"
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of an object
        """
        return self.title

    def get_absolute_url(self):
        """
        For be able to edit the article and redirect user back the same article
        """
        return reverse("post_detail", args=[str(self.slug)])
