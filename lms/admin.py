from django.contrib import admin

from lms.models import Lesson, Course, Payments

admin.site.register(Lesson)

admin.site.register(Course)

admin.site.register(Payments)
