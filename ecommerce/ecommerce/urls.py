"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from EApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Dashboard),

    path('shop/',TemplateView.as_view(template_name='shop.html')),
    path('contact/',TemplateView.as_view(template_name='contact.html')),
    path('cart/',TemplateView.as_view(template_name='cart.html')),
    path('product/',TemplateView.as_view(template_name='product.html')),
    path('regular/',TemplateView.as_view(template_name='regular.html')),
    path('blog/',TemplateView.as_view(template_name='blog.html')),
    path('blog_single/',TemplateView.as_view(template_name='blog_single.html')),
]
