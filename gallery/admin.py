from posixpath import join
from django.contrib import admin

# Register your models here.
from gallery.models import Gallery, Category


class Gallery_Admin(admin.ModelAdmin):
    list_display = ["__str__", "alt", "status", "image", "get_categories"]
    list_editable = ["status", "alt"]
    ordering = ["position", ]

    def get_categories(self, obj):
        return "، ".join([i.title for i in obj.categories_active()])
    get_categories.short_description = "دسته بندی"

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        try:
            counter = int(
                Gallery.objects.all().last().position) + 1
        except:
            counter = 1
        form.base_fields["position"].initial = counter
        return form


class Category_Admin(admin.ModelAdmin):
    list_display = ["__str__", "status", "slug"]
    list_editable = ["status", "slug"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["status", ]


admin.site.register(Gallery, Gallery_Admin)
admin.site.register(Category, Category_Admin)
