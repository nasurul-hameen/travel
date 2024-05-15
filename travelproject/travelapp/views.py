# from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo(request):
    return render(request, "index.html")


# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     a = x + y
#     s = x - y
#     m = x * y
#     d = x / y
#     return render(request, "result.html", {'add': a, 'sub': s, 'mul': m, 'div':d})
