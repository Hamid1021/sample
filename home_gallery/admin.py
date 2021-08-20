from django.contrib import admin

# Register your models here.
from home_gallery.models import Gallery_Home


class Gallery_Home_Admin(admin.ModelAdmin):
    list_display = ["__str__", "status", "image"]
    list_editable = ["status",]
    ordering = ["position", ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        try:
            counter = int(
                Gallery_Home.objects.all().last().position) + 1
        except:
            counter = 1
        form.base_fields["position"].initial = counter
        return form


admin.site.register(Gallery_Home, Gallery_Home_Admin)
