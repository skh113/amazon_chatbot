from django.shortcuts import render

# Create your views here.


def error_404(request):
    data = {}
    return render(request, "404.html", data)
