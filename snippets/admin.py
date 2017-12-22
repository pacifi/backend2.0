from django.contrib import admin
from .models import Snippet


@admin.register(Snippet)
class SnippetSerializer(admin.ModelAdmin):
    pass
