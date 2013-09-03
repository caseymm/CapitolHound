# Create your views here.

from django.shortcuts import render

def home(request):
    context = {'message': 'Here\'s the message from the views file'}
    return render(request, "base.html", context)
