from django.shortcuts import get_object_or_404, render

from .models import Post


# MARK: - Actions

def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'posts/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})
