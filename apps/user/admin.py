from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

User = get_user_model()

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin


class UserResource(ModelResource):
    def __init__(self, *args, **kwargs):
        super(UserResource, self).__init__(*args, **kwargs)
        self.fields['id'].column_name = _('ID')
        self.fields['first_name'].column_name = _('First name')
        self.fields['last_name'].column_name = _('Last name')
        self.fields['phone_number'].column_name = _('Phone number')
        self.fields['telegram_id'].column_name = _('Telegram id')
        self.fields['created_at'].column_name = _('Created at')
    
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'telegram_id',
            'created_at',
        )

@admin.register(User)
class UserAdmin(ImportExportModelAdmin, DjangoUserAdmin):
    resource_classes = [UserResource]
    readonly_fields = ('last_login', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('phone_number', 'password')
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'profile', 'telegram_id')
        }),
        (_('Permissions'), {
            'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')
        }),
        (_("Important dates"), {
            'fields': ('created_at', 'last_login')
        })
    )
    list_display = ('phone_number', 'first_name', 'last_name', 'telegram_id', 'created_at')    
    list_display_links = ('phone_number',)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "usable_password", "password1", "password2"),
            },
        ),
    )
    search_fields = ("phone_number", "first_name", "last_name", "telegram_id", "id")
    ordering = ("-created_at",)
        
