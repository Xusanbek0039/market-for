"""Easykeyboardmaker URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from .views import handler403, handler404, handler405, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('information/', include('home.urls')),
    path('support/', include('home.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('bag/', include('bag.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error handling 
handler403 = 'Easykeyboardmaker.views.handler403'
handler404 = 'Easykeyboardmaker.views.handler404'
handler405 = 'Easykeyboardmaker.views.handler405'
handler500 = 'Easykeyboardmaker.views.handler500'
