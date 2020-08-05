from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Type)
admin.site.register(Animal)
admin.site.register(Room)
admin.site.register(Comment)
