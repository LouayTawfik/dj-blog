"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from blog.views import post_create, post_delete, post_detail, post_list, post_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/list', post_list),
    path('post/detail/<int:post_id>', post_detail),
    path('post/new', post_create),
    path('post/update/<int:post_id>', post_update),
    path('post/delete/<int:post_id>', post_delete)
]
