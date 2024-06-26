from django.contrib import admin
from .models import hiring


admin.site.register(hiring)
# @admin.register(hiring)
# class CareerModel(admin.ModelAdmin):
#     # for showing the Jalali date on the list_display, please change the LIST_DISPLAY_AUTO_CONVERT to true or create custom methods. for example:
#     list_display = ['firstName','lastName']
