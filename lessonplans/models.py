from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Lessonplan(models.Model):
    CLASS_CHOICES = (
        ("10","10"),
        ("9","9"),
        ("8","8"),
        ("7","7"),
        ("6","6"),
        ("5","5"),
        ("4","4"),
        ("3","3"),
        ("2","2"),
        ("1","1"),
    )
    lessonplan_class = models.CharField(max_length=2,choices=CLASS_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

