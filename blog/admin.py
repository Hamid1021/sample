from django.contrib import admin
from django.utils import timezone
from blog.models import Article, Category, Comment
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', "slug", "status")
    list_editable = ("status",)
    list_filter = (['status'])
    search_fields = ('title', "slug",)
    prepopulated_fields = {"slug": ("title",)}



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', "slug", "category_to_str", "jpublish", "status")
    list_filter = ('publish', 'status')
    list_editable = ("status",)
    search_fields = ('title', "slug", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["-publish", "-status"]

    def category_to_str(self, obj):
        return ", ".join([i.title for i in obj.category_published()])
    category_to_str.short_description = "دسته بندی"

    def save_model(self, request, obj, form, change):
        obj.publish = timezone.localtime(timezone.now())
        print(obj.publish)
        super(ArticleAdmin, self).save_model(request, obj, form, change)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('fullname', "email", "jcreated", "article", "status",)
    list_filter = ('status',)
    list_editable = ("status",)
    search_fields = ('status', "status", "message",)
    readonly_fields = ["jcreated", "created", "article",]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
