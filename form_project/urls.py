"""
URL configuration for form_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import form_example.views

urlpatterns = [
    path("", form_example.views.index),
    path("admin/", admin.site.urls),
    path("form-example/", form_example.views.form_example),
    path("django-form/", form_example.views.form_django_example),
    path("success-page/", form_example.views.user_login),
    path("user_login/", form_example.views.user_login),
    path("newsletter/" , form_example.views.newsletter),
    path("order/", form_example.views.order),
    path("placeholder/", form_example.views.example_placeholder),
    path("publishers/<int:pk>", form_example.views.publisher_edit, name="publisher_edit"),
    path("publishers/new/", form_example.views.publisher_edit, name="publisher_create")

    # path("view_func/", form_example.views.view_function),
]
