from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request,"dictionary/home.html")

def search_view(request):
    return render(request,"dictionary/search.html")