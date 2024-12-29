from django.contrib import admin

from lms.models import Course, Lesson, Payment


admin.site.register(Lesson)

admin.site.register(Course)

admin.site.register(Payment)
