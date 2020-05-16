from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Article,Category,Author,Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
#for Search import QLookUp
from django.db.models import Q
#for createPost from import
from .forms import CreateFrom , UserRegistration , CreateAuthor ,CommentForm , CreateCategory
#for message
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World .. </h1>")
    allArticle = Article.objects.all()
    ''' search Code Start '''
    search = request.GET.get('search')
    if search:
        allArticle = allArticle.filter(
            Q(title__icontains=search)
        )

    ''' Pagination Code Start '''
    paginator = Paginator(allArticle, 8) # Show 25 contacts per page.

    page = request.GET.get('page')
    total_article = paginator.get_page(page)

    return render(request,'index.html' , {'allArticle':total_article})

def profile(request):
    return render(request, 'profile.html')

def article(request , id):
    singlePost = get_object_or_404(Article , id=id)
    postComment=Comment.objects.filter(id=id)
    related    = Article.objects.filter(category = singlePost.category).exclude(id=id)[:4]
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.post = singlePost
        instance.save()
    context={
        "data":singlePost,
        "related":related,
        "form":form,
        "postComment":postComment
    }
    return render(request, "single.html",context)

def getCategory(request , name):
    cat = get_object_or_404(Category , name=name)
    post = Article.objects.filter(category=cat.id)
    return render(request, "category.html",{'post':post ,'cat':cat})


def getLogin(request):
    if request.user.is_authenticated:
        return redirect('blog:index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('blog:index')
            else:
                messages.add_message(request, messages.ERROR, 'UserName Or Password mismatch')
    return render(request, "login.html")


def getLogout(request):
    logout(request)
    return redirect('blog:index')


def getAuthor(request , name):
    post_author = get_object_or_404(User , username=name)
    auth = get_object_or_404(Author , name= post_author.id)
    post = Article.objects.filter(article_author=auth.id)
    context={
        "auth":auth,
        "post":post
    }
    return render(request , "profile.html",context)

#for CreatePost Page
def getCreatePost(request):
    if request.user.is_authenticated:
        user =get_object_or_404(Author , name=request.user.id)
        form=CreateFrom(request.POST or None , request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author = user
            instance.save()
            return redirect('index') 
        return render(request , "postCreate.html",{'form':form})
    else:
        return redirect('login')

def getProfile(request):
    if request.user.is_authenticated:
        user =get_object_or_404(User , id=request.user.id)
        author_profile=Author.objects.filter(name=user.id)
        if author_profile:
            authorUser=get_object_or_404(Author , name=request.user.id)
            post = Article.objects.filter(article_author=authorUser)
            return render(request , "logged_in_profile.html" , {'post':post ,'user':authorUser})
        else:
            form=CreateAuthor(request.POST or None , request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.name = user
                instance.save()
            return render(request , "createAuthorProfile.html",{"form":form}) 

    else:
        return redirect('login')
        
def getUpdate(request, id):
    if request.user.is_authenticated:
        user =get_object_or_404(Author , name=request.user.id)
        post =get_object_or_404(Article , id=id)
        form=CreateFrom(request.POST or None , request.FILES or None , instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author = user
            instance.save()
            messages.success(request, 'Post details updated.')
            return redirect('logged_in_profile') 
        return render(request , "postCreate.html",{'form':form})
    else:
        return redirect('login')


def getDelete(request, id):
    if request.user.is_authenticated:
        post=get_object_or_404(Article, id=id)
        post.delete()
        return redirect('logged_in_profile')
    else:
        return redirect('login')

def getRegistern(request):
    form = UserRegistration(request.POST or None , request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Registration Successfully..')
        return redirect('login')

    return render(request , "registration.html",{"form":form})


def getAllCategory(request):
    allCategory = Category.objects.all()
    return render(request , "allCategory.html",{"allCategory":allCategory})

def getCreateCategory(request):
    form = CreateCategory(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request , "Category Create Successfully")
        return redirect('blog:allCategory')
    return render(request , "createCategory.html",{"form":form})