from django.contrib import admin

# Register your models here.
from .models import AboutUs, Why_Choose_US, Chef

admin.site.register(AboutUs)
admin.site.register(Why_Choose_US)
admin.site.register(Chef)