from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from account.models import User
from extensions.utils import jalali_converter_date

class UserAdmin(UserAdmin):
    fieldsets = (
        ("اطلاعات کاربری", {'fields': ('username', 'password', 'pass_per_save')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'gender', 'email', 'image')}),
        ("اطلاعات ثبت نام", {'fields': ('custom_user_id', 'code_send', 'email_sended', 'phone_number')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ("pass_per_save",)
    add_fieldsets = (
        ("اطلاعات کاربری", {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'phone_number', 'email', 'first_name', 'last_name', "is_active", 'is_staff', "is_superuser")
    list_display_links = ('username', 'phone_number')
    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
		
admin.site.register(User, UserAdmin)
