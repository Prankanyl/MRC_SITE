from django.contrib import admin
from main_app import models


admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Specialty)
admin.site.register(models.Practice)

# Register your models here.
