from django.contrib import admin
from .models import HomePageContent
from django_summernote.admin import SummernoteModelAdmin

@admin.register(HomePageContent)
class HomePageAdmin(SummernoteModelAdmin):

    search_fields = ['header']
    summernote_fields = ('content',)

# Register your models here.
