from django.db import models

class MyApp(models.Model):
    key = models.TextField(max_length=100, primary_key=True)
    count = models.IntegerField(default=0)