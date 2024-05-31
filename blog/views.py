from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm


class PostList(ListView):
    """
    ListView for displaying a paginated list of blog posts
    """
    model = Post
    template_name = "blog/blog.html"
    context_object_name = "posts"
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset().filter(status=1)
        query = self.request.GET.get("q")
        sort = self.request.GET.get("sort")
        direction = self.request.GET.get("direction")

        if sort:
            if sort == "created_on":
                sortkey = (
                    sort if not direction or direction == "asc" else f"-{sort}"
                )
            else:
                sortkey = f"-{sort}" if direction == "desc" else sort
            queryset = queryset.order_by(sortkey)
        if query:
            queries = Q(title__icontains=query) | Q(excerpt__icontains=query)
            queryset = queryset.filter(queries)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        context["current_sorting"] = (
            f"{self.request.GET.get('sort')}_"
            f"{self.request.GET.get('direction')}"
        )
        return context


class PostDetail(View):
    """
    Class & Method to call the articles details pages
    """
    template_name = "blog/post_detail.html"

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = {"post": post}
        return render(request, self.template_name, context)


class PostDelete(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """
    View for deleting an existing blog Article
    """
    model = Post
    template_name = "blog/post_delete.html"
    success_message = "Article is deleted!"
    success_url = reverse_lazy("blog")

    def test_func(self):
        """
        Check if the current user is admin for
        being able to delete post
        """
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class PostCreate(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    """
    View for creating a new blog Article
    """
    model = Post
    template_name = "blog/post_create.html"
    form_class = PostForm
    success_message = "Article has been created"
    success_url = reverse_lazy("blog")

    def test_func(self):
        """
        Check if the current user is a superuser (admin)
        """
        return self.request.user.is_superuser

    def form_valid(self, form):
        """
        Custom logic to handle form validation when creating a new blog post
        """
        form.instance.author_id = self.request.user.pk
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostEdit(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    View for editing an existing Article
    """
    model = Post
    template_name = "blog/post_edit.html"
    form_class = PostForm
    success_message = "Article updated successfully"

    def test_func(self):
        """
        Check if the current user is the author of the post being updated
        """
        post = self.get_object()
        return self.request.user.is_superuser

    def get_success_message(self, cleaned_data=None):
        return self.success_message
