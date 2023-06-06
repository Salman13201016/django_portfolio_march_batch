from django.db import models

class About(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 500)
    email = models.EmailField(max_length = 500)
    bg = models.CharField(max_length = 500)
    fb = models.CharField(max_length = 500)