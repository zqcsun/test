from django.shortcuts import render,redirect
from .models import Post
from .forms import CreateForm

def list_post(request):
    posts = Post.objects.all() 
    """
    [{title:"Python",...},{},{}]
    """
    context = {'posts':posts}
    return render(request,'listpost.html',context)

def post(request, slug, id):
    post = Post.objects.get(slug = slug, id = id)
    context = {'post':post}
    return render(request,'post.html', context)
# Create your views here.

def create_post(request):
    form = CreateForm()
    if request.POST:
        form = CreateForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit = False)
            new_post.user = request.user
            new_post.save()
            return redirect("None")
    else:
        form = CreateForm()

    return render(request,'',{'form':form})