from django.db import models
from django.forms import SelectDateWidget

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title