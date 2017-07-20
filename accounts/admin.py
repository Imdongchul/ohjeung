from django.contrib import admin
from .models import Post,Comment,Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass
