from django.contrib import admin
from .models import Toy, Status, Division, Category

admin.site.register(Toy)
admin.site.register(Status)
admin.site.register(Division)
admin.site.register(Category)
# Register your models here.
