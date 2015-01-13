from django.contrib import admin
from mortimer.models import AppID, AppData

# Temporarily give admin access to view all app data

admin.site.register(AppID)
admin.site.register(AppData)