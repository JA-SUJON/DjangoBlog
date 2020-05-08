from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Article

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World .. </h1>")
    allArticle = Article.objects.all()
    return render(request,'index.html' , {'allArticle':allArticle})

def profile(request):
    return render(request, 'profile.html')

def article(request , id):
    singlePost = get_object_or_404(Article , id=id)
    context={
        "data":singlePost
    }
    return render(request, "single.html",context)

def getCategory(request , name):
    return render(request, "category.html")