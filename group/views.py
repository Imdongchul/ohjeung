from django.shortcuts import render

def group_index(request):
    return render(request, 'group/group_index.html')

def group_make(request):
    return render(request, 'group/group_make.html')
# Create your views here.
