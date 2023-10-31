from django.shortcuts import render, HttpResponse


def index_view(request):
    return render(request, 'website/home.html')


def profile_view(request):
    return render(request, 'website/profile.html')


def contact_view(request):
    return render(request, 'website/contact.html')
