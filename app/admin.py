from django.contrib import admin
from app.models import Data,UserRegistartion

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display=['name','browser']
    
admin.site.register(Data,DataAdmin)


class UserRegistartionAdmin(admin.ModelAdmin):
    list_display=['name','adhar_number','mobile_number','address','age','UID']
    
admin.site.register(UserRegistartion,UserRegistartionAdmin)
