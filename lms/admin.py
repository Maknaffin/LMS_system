from django.contrib import admin

from lms.models import Lesson, Course, Payment

admin.site.register(Lesson)

admin.site.register(Course)

admin.site.register(Payment)
