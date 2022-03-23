from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment




class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')





admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
