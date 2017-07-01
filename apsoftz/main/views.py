from django.shortcuts import render

def index(request):
    return render(request,'main/index.html',{})

def about(request):
    return render(request,'main/about.html',{})

def contact(request):
    return render(request,'main/contact.html',{})

def social(request):
    return render(request,'main/social.html',{})

def git(request):
    return render(request,'main/git.html',{})
