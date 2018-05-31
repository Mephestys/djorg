from django.contrib import admin
from .models import Tag, Note

@admin.register(Note, Tag)
class AuthorAdmin(admin.ModelAdmin):
  pass