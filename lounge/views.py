from django.shortcuts import render

# Create your views here.
def lounge(request):
    return render(request, 'lounge/lounge.html')
