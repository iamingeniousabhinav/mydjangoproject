from multiprocessing import context
from unittest import result
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

def calculator(request):  # sourcery skip: do-not-use-bare-except
    c = ''
    try:
        if request.method == 'POST':
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == '+':
                c = n1+n2
            elif opr == '-':
                c = n1-n2
            elif opr == '*':
                c = n1*n2
            elif opr == '/':
                c = n1/n2
    except:
        c = 'error'

    result = {
                'c':c
            }
    return render(request, 'calculator.html',result )