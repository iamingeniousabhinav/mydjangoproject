from django.shortcuts import render
from .models import *

# call your data from models


# Create your views here.
def index(request):
    return render(request, 'index.html')