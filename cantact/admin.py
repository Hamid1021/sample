from django.contrib import admin

# Register your models here.
from cantact.models import Message


class Message_Admin(admin.ModelAdmin):
    list_display = ["full_name", "email", "subject", "jsend_time", "status"]
    list_filter = ["status",]
    readonly_fields = ["full_name", "email", "subject", "message", "jsend_time", "send_time", "status",]
    
    def save_model(self, request, obj, form, change):
        obj.status = "r"
        super(Message_Admin, self).save_model(request, obj, form, change)

admin.site.register(Message, Message_Admin)
