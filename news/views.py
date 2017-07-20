from django.shortcuts import redirect, get_object_or_404, render
from accounts.models import Post,Comment
from accounts.forms import CommentModelForm
from django.utils import timezone
import json


def news_list(request, pk=None):
	post = Post.objects.all()
	post = post.order_by('-id')

	form = CommentModelForm(request.POST or None)
	if pk == None:
		pass
	else:
		post = get_object_or_404(Post, pk=pk)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = request.user
			comment.post_id = post.id
			comment.created_at = timezone.now()
			comment.save()
			return redirect('news:news_list')
	return render(request, 'news/news_list.html',{
		'post_list':post,
		'form':form,
		})



