from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ShopCategory

class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'phone', 'shop_category')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone', 'image', 'address', 'shop_category')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone', 'image', 'address', 'shop_category')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ShopCategory, ShopCategoryAdmin)
