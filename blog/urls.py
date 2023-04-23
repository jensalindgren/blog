from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("",
         views.PostList.as_view(),
         name="home"),

    path("post_detail/<slug:slug>/",
         views.PostDetailView.as_view(),
         name="post_detail"),

    path('post_post/',
         views.AddPostView.as_view(),
         name='add_post'),

    path('delete_post/<slug:slug>/',
         views.DeletePostView.as_view(),
         name='delete_post'),


    path('edit_post/<int:id>/',
         views.EditPostView.as_view(),
         name='edit_post'),

    path(
        'post_comment/<int:post_id>/',
        views.PostCommentView.as_view(),
        name='post_comment'),

    path('404',
         TemplateView.as_view(template_name='404.html'),
         name='404'),

    path('delete_comment/<int:id>/',
         views.CommentDeleteView.as_view(),
         name='delete_comment'),
]
