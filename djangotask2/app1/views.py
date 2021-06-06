from django.shortcuts import render

# Create your views here.


def loadhome(request):
    return render(request, "home.html")


def loadregister(request):
    return render(request, "registrationform.html")


def loadlogin(request):
    return render(request, "login.html")
