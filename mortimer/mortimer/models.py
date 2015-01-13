from django.db import models

class AppID(models.Model):
    app_name = models.CharField(max_length=100)
    app_desc = models.CharField(max_length=500)

class AppData(models.Model):
    app_id = models.ForeignKey(AppID)
    username = models.CharField(max_length=20)
    enc_password = models.CharField(max_length=32)

