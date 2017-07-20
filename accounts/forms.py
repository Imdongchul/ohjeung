from django import forms
from .models import Post, Comment,Profile
from django.contrib.auth.forms import UserCreationForm


class PostModelForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'photo']


class CommentModelForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['message']

class SignupForm(UserCreationForm):
	phone_number = forms.CharField()
	address = forms.CharField()

	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ('email',)


	def save(self):
		user = super().save() #새로운 user인스턴스가 만들어지고 save가 됨
		profile = Profile.objects.create(
			user = user,
			phone_number = self.cleaned_data['phone_number'],
			address = self.cleaned_data['address']) # 새로운 유저인스턴스를 가지고 프로필을 새롭게 생성한다.
		return user