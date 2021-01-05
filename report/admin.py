from django.contrib import admin
from .models import Person, Url, Url_data, Query, Exception, Report

admin.site.register(Person)
admin.site.register(Url_data)
admin.site.register(Url)
admin.site.register(Query)
admin.site.register(Exception)
admin.site.register(Report)


# Register your models here.
