from django.contrib import admin

# Register your models here.

from seo.models import Seo


class Seo_Admin(admin.ModelAdmin):
    list_display = ["site_name", "owner", "status",
                    "url", "time_work_start", "time_work_end",]
    list_editable = ["status", "owner",]



admin.site.register(Seo, Seo_Admin)
