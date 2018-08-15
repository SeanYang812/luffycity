from django.contrib import admin

# Register your models here.

from app01 import models

admin.site.register(models.Course)

admin.site.register(models.CourseDetail)

admin.site.register(models.Teacher)

admin.site.register(models.PricePolicy)

admin.site.register(models.Chapter)

admin.site.register(models.CourseSection)

admin.site.register(models.OftenAskedQuestion)



admin.site.register(models.User)

admin.site.register(models.UserToken)