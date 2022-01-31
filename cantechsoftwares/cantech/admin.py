from django.contrib import admin

from cantech.models import FeedbackModel

# Register your models here.

@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['f_name','f_phoneno','f_email']