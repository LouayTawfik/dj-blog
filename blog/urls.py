from django.urls import path, include

from blog.views import post_create, post_delete, post_detail, post_update, post_list


urlpatterns = [
    path('post/new', post_create.as_view()),
    path('post/list', post_list.as_view()),
    path('post/detail/<int:pk>', post_detail.as_view()),
    path('post/update/<int:pk>', post_update.as_view()),
    path('post/delete/<int:pk>', post_delete.as_view())
]