from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

<<<<<<< HEAD
# Create your views here.
<<<<<<< HEAD
=======
def post_list(request):
	return render(request, 'blog/post_list.html',{})
>>>>>>> 6a018f7998af115da34b08cfb3ca5817130be73d
=======
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
>>>>>>> 4821428907749cd52bb703f3946daaa4be0b5576
