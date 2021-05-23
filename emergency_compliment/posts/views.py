from django.shortcuts import render

from .models import Post


# MARK: - Actions

def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'posts/index.html', context)
