from django.shortcuts import render, redirect

def index(request):
    print 'Hello World'
    return render(request, 'helloWorld_app/index.html')
