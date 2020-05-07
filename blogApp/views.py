from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World .. </h1>")
    return render(request,'index.html')

def profile(request):
    return render(request, 'profile.html')

def article(request , id):
    return render(request, "single.html")