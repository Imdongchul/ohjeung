from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
	title = models.CharField('제목', max_length=20)
	content = models.TextField('내용')
	photo = models.ImageField('사진', blank=True)
	create_at = models.DateTimeField('게시일', auto_now_add=True)
	updated_at = models.DateTimeField('수정일', auto_now=True)

class Comment(models.Model):
	post = models.ForeignKey(Post)
	message = models.CharField(max_length=50)
	author = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	phone_number = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
