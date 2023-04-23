from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class postAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'author', 'created_on', )
    search_fields = ('title', 'content', 'author__username')
    action = ('approve_post')

    def approve_post(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved', 
                    'last_updated', '__str__',)
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body', 'author__username')
    actions = ('approve_comments')

    def approve_comments(self, request, queryset):
        queryset.update(active=True)