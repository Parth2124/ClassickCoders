from django.contrib import admin
from .models import courses,jobs,internships
# Register your models here.

admin.site.register(courses)
admin.site.register(jobs)
admin.site.register(internships)