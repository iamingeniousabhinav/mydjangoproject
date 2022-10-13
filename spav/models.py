from django.db import models

# Create your models here.

class Noticeboard(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='Noticeboard', max_length=100)
    upload_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title