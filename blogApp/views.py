from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Article,Category,Author
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
#for Search import QLookUp
from django.db.models import Q
#for createPost from import
from .forms import CreateFrom

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
    related    = Article.objects.filter(category = singlePost.category).exclude(id=id)[:4]
    context={
        "data":singlePost,
        "related":related
    }
    return render(request, "single.html",context)

def getCategory(request , name):
    cat = get_object_or_404(Category , name=name)
    post = Article.objects.filter(category=cat.id)
    return render(request, "category.html",{'post':post ,'cat':cat})


def getLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
    return render(request, "login.html")


def getLogout(request):
    logout(request)
    return redirect('index')


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
        form=CreateFrom(request.POST or None , request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save();
            return redirect('index') 
        return render(request , "postCreate.html",{'form':form})
    else:
        return redirect('login')
        

