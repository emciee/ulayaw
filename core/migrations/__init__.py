from django.shortcuts import render


def phil(request):
    return render(request, "core/philmen.html")