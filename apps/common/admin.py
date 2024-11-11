from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from apps.common import models

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin



# @admin.register(models.VersionHistory)
# class VersionHistoryAdmin(admin.ModelAdmin):
#     list_display = ("id", "version", "required", "created_at", "updated_at")
#     list_display_links = ("id", "version")
#     list_filter = ("required", "created_at", "updated_at")
#     search_fields = ("version",)


class ProductSizeInline(admin.TabularInline):
    model = models.ProductSize
    extra = 1
    readonly_fields = ('name', 'description',)
    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline]
    list_display = ('name', 'image_preview', 'created_at')

    fieldsets = (
        (_('Main'), {
            'fields': ('name', 'description', 'image', 'category')
        }),
        (_('Uzbek'), {'fields': ('name_uz', 'description_uz')}),
        (_('Russian'), {'fields': ('name_ru', 'description_ru')})
    )    
    
    readonly_fields = ('name', 'description')

    def image_preview(self, obj):

        if obj.image:
            try:
                photo = models.Product.objects.get(id=obj.id)
            except models.Product.DoesNotExist:
                return "(No image)"

            return mark_safe(
                '<img src="{0}" width="100" height="100" style="object-fit:contain" />'.format(photo.image.url)
            )
        else:
            return "(No image)"


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_type', 'created_at')
    list_display_links = ('name', )
    readonly_fields = ('name', )


class CartItemInline(admin.TabularInline):
    model = models.CartItem
    extra = 1
    readonly_fields = ('product', 'quantity')


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ('user__phone_number', )
    list_display_links = ('user__phone_number',)
    

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 1
    readonly_fields = ('product', 'quantity')

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('user__phone_number', 'status', 'delivery_time', 'is_discount')
    list_display_links = ('user__phone_number',)
    list_filter = ('status', 'is_discount')    


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_display_links = ('title', )


admin.site.register(models.Rating)
