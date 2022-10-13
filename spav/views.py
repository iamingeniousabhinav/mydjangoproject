from multiprocessing import context
from django.shortcuts import render
from .models import *

# call your data from models

notice_data = Noticeboard.objects.all()


context = {
    'notice_data' : notice_data
}

# Create your views here.
def index(request):
    return render(request, 'index.html', context)

def noticeboard(request):
    return render(request, 'noticeboard.html', context)