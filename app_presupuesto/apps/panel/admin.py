from django.contrib import admin
from .models import *

# Register your models here.
class TypeBudgetAdmin(admin.ModelAdmin):
    list_display=("title",)

admin.site.register(TypeBudget,TypeBudgetAdmin)