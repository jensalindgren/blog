from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class postAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on', 'last_updated')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'last_updated')
    search_fields = ('title', 'content', 'author__username')

    summernote_fields = ('content')


@admin.register(Comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'created_on', 'post')
    list_filter = ('created_on', 'author', 'post')
    search_fields = ('body', 'author__username')

    summernote_fields = ('body')