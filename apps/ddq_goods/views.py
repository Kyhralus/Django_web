from django.shortcuts import render
from . import views
# Create your views here.

# http://127.0.0.1:8000
def index(request):
    """显示首页"""
    return render(request, "index.html")