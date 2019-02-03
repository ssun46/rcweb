from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def done(request, msg=None):
    return render(request, 'done.html', dict(msg=msg))