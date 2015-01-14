from django.db import models
from django.contrib.auth.models import User

class AppID(models.Model):
    app_user = models.ForeignKey(User)
    app_name = models.CharField(max_length=100)
    app_desc = models.CharField(max_length=500)

    class Meta:
        unique_together = (("app_user","app_name"),)

class AppData(models.Model):
    app_id = models.ForeignKey(AppID)
    username = models.CharField(max_length=25)
    enc_password = models.CharField(max_length=64)

    class Meta:
        unique_together = (("app_id","username"),)

