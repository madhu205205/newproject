from django.contrib import admin

# Register your models here.
from .models import College,Branch
admin.site.register(College)
admin.site.register(Branch)
