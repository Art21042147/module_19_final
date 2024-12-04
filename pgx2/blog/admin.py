from django.contrib import admin
from .models import User, BlogPost, Category, Media, Docs


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'size', 'description', 'age_limited')
    search_fields = ('title',)


@admin.register(Docs)
class DocsAdmin(admin.ModelAdmin):
    list_display = ('title', 'size')
    search_fields = ('title',)
