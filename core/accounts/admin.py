from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import User , Profile
# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email','is_superuser','is_active')
    list_filter = ('email','is_superuser','is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('authentication' , {
            "fields":(
                'email','password'
            ),
        }),
        ('permissions' , {
            'fields' : (
                'is_staff','is_active' , 'is_superuser'
            ),
        }),
        ('group permission' , {
            'fields' : (
                'groups','user_permissions'
            ),
        }),
        ('importantt date' , {
            'fields' : (
                'last_login','created_date',
            ),
        }),
    )
    readonly_fields=('last_login','created_date')
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email","password1", "password2","is_staff","is_active","is_superuser"],
            },
        ),
    ]

admin.site.register(Profile)