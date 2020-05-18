from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
# post_list를 view에서 보여줌
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

