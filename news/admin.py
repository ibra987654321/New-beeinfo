from django.contrib import admin
from .models import LatestProblems


@admin.register(LatestProblems)
class ProblemsAdmin(admin.ModelAdmin):
    fields = ['description', 'date_created', 'date_updated', 'status', 'comment']
    list_display = ['description', 'date_created', 'date_updated', 'status', 'comment']