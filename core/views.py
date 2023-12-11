from django.shortcuts import render

# Create your views here.

#homepage
def home(request):
    return render(request, "core/homepage.html")

#aboutus page
def aboutus(request):
    return render(request, "core/aboutuspage.html")

#mental health library page
def mhl(request):
    return render(request, "core/mhlpage.html")