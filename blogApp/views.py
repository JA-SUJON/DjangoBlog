from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Article,Category

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World .. </h1>")
    allArticle = Article.objects.all()
    return render(request,'index.html' , {'allArticle':allArticle})

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