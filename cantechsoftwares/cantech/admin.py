from django.contrib import admin

from cantech.models import *

# Register your models here.

@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['f_name','f_phoneno','f_email']


admin.site.register(QuotationModel)