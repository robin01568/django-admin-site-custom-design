"""
URL configuration for fametours project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    # Admin panel
    path('grappelli/', include('grappelli.urls')),
    path('rs/fame/', admin.site.urls),
    
    # Application URLs
    path('', include('indexApp.urls')),

    # CKEditor URL for media uploads
    path('ckeditor/', include('ckeditor_uploader.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]




# Custom error handlers
handler404 = 'indexApp.views.page_not_found'
handler500 = 'indexApp.views.internal_error'
