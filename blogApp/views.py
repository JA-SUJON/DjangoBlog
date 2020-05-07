from django.shortcuts import render,HttpResponse
from .models import Article

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World .. </h1>")
    allArticle = Article.objects.all()
    return render(request,'index.html' , {'allArticle':allArticle})

def profile(request):
    return render(request, 'profile.html')

def article(request , id):
    return render(request, "single.html")

def getCategory(request , name):
    return render(request, "category.html")