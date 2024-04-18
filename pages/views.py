from django.shortcuts import render,redirect
from .models import Post
from .form import PostForm


# Create your views here.

def index(request):
    topic = request.GET.get('topic')
    if topic:
        posts = Post.objects.filter(topic=topic)
    else:
        posts = Post.objects.all()
    return render(request,'pages/index.html', {'posts': posts})



def newPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = PostForm()        
    return render(request, 'pages/newPost.html', {'form': form})



def aboutPost(request):
    post_id = request.GET.get('id')
    post = Post.objects.filter(id=post_id).first()
    

    return render(request,'pages/aboutPost.html', {'post': post})

