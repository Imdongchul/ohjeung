from django.shortcuts import redirect,get_object_or_404,render
from .models import Post,Comment,Profile
from .forms import PostModelForm, CommentModelForm, SignupForm
# from django.contrib.auth.forms import UserCreationForm

from django.conf import settings


#index_all 모든 유저가 보는 메인 페이지
#회원이 보는 메인 페이지

def index(request):
	a = "오제웅병신"
	if request.method == 'POST':
		form = PostModelForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save
			return redirect('news:news_list')
	else:
		form = PostModelForm()
	return render(request,'accounts/index.html',{
		'form':form,
		'a':a,
		})

# def joinus(request):
#     return render(request, 'accounts/joinus.html')

def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect(settings.LOGIN_URL)
	else:
		form = SignupForm()
	return render(request, 'accounts/joinus.html',{
		'form':form,
		})

def profile(request):
	return render(request,'accounts/index.html')






