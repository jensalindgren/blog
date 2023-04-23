from . import views
from django.urls import path

urlpatterns = [
    path("",
         views.PostList.as_view(),
         name="home"),

    path("post/<slug:slug>/",
         views.PostDetail.as_view(),
         name="post_detail"),

    path('post_post/',
         views.AddPost.as_view(),
         name='add_post'),

    path('edit_post/<int:id>/',
         views.EditPost.as_view(),
         name='edit_post'),

    path('delete_post/<slug:slug>/',
         views.DeletePost.as_view(),
         name='delete_post'),

    path(
        'post_comment/<int:post_id>/',
        views.AddComment.as_view(),
        name='post_comment'),

    path('delete_comment/<int:id>/',
         views.DeleteComment.as_view(),
         name='delete_comment'),

    path('edit_comment/<int:id>/',
         views.EditComment.as_view(),
         name='edit_comment'),
]