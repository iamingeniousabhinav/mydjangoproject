from multiprocessing import context
from unittest import result
from django.shortcuts import render
from .models import *

# call your data from models

notice_data = Noticeboard.objects.all().order_by('-upload_date')
flashNewsData = FlashNews.objects.all().order_by('-upload_date')
tenderData = Tender.objects.all().order_by('-upload_date')
recruitmentData = Recruitment.objects.all().order_by('-upload_date')
upcomingLectures = UpcomingLecture.objects.all().order_by('-upload_date')
circularsData = Circulars.objects.all().order_by('-upload_date')
weatherData = WeatherReport.objects.all().order_by('-upload_date')

context = {
    'notice_data' : notice_data,
    'tender':tenderData,
    'flashNews':flashNewsData,
    'recruitment':recruitmentData,
    'circulars':circularsData,
    'upcomingLectures':upcomingLectures,
    'weather':weatherData,
}

# Create your views here.
def index(request):
    return render(request, 'index.html', context)

def weather_report(request):
    return render(request, 'weather_report.html', context)

def about(request):
    return render(request, 'about.html', context)

def campus_view(request):
    return render(request, 'campus.html', context)

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