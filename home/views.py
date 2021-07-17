from django.shortcuts import render


def index(request):
    """Returns the index page"""

    return render(request, 'home/index.html')

def error_404(request, *args, **kwargs):
    data = {}
    return render(request,'home/404.html', data)

def error_500(request, *args, **kwargs):
    data = {}
    return render(request,'home/500.html', data)
