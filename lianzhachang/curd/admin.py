from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.UserInfo)
admin.site.register(models.JobTitle)
admin.site.register(models.Position)
admin.site.register(models.OperatingArea)
admin.site.register(models.Profession)