from .models import Post, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    """ Form for Post submission """
    class Meta:
        model = Post
        fields = ['title', 'content',]
        widgets = {
            'content': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    """ Form for Comments submission """
    class Meta:
        model = Comment
        fields = ['body',]
        widgets = {
            'content': SummernoteWidget(),
        }
