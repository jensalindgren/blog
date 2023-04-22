from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class postAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    action = ('approve_post')

    def approve_post(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ('approve_comments')

    def approve_comments(self, request, queryset):
        queryset.update(active=True)