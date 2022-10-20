from django.db import models

# Create your models here.

class FlashNews(models.Model):
    flash_news_title = models.CharField(max_length=250)
    file = models.FileField(upload_to='Noticeboard', max_length=100)
    upload_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.flash_news_title


class Noticeboard(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='Noticeboard', max_length=100)
    upload_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title

class Tender(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='Noticeboard', max_length=100)
    upload_date = models.DateField(auto_now=False, auto_now_add=False)
    last_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title

class UpcomingLecture(models.Model):
    lecture_title = models.CharField(max_length=250)
    file = models.FileField(upload_to='Noticeboard', max_length=100)
    link = models.URLField(max_length=200, null = True)
    upload_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.lecture_title

class Recruitment(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='Noticeboard', max_length=100)
    link = models.URLField(max_length=200, null = True)
    upload_date = models.DateField(auto_now=False, auto_now_add=False)
    last_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title

class Circulars(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='Noticeboard', max_length=100)
    upload_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title

class WeatherReport(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='Noticeboard', max_length=100)
    upload_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title

