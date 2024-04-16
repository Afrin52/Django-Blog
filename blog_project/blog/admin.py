from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Comment, CommentLike, Tag, Blog
# Register your models here.
admin.site.unregister(Group)
# admin.site.register(Comment)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'content','created_at')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog', 'created_at', 'content')
    list_filter = ('active', 'created_at')
    search_fields = ('email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Blog, BlogAdmin)
# admin.site.register(Blog)
admin.site.register(Tag)
# admin.site.register(User)
admin.site.register(CommentLike)