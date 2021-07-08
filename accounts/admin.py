from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import User
from .forms import UserAdminCreationsForm
# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin):
    readonly_fields=('slug','last_update')
    
    fieldsets = (
        (_('Personal info'), {'fields': ('username','first_name', 'last_name', 'email','phone_number','image','country', 'city','password')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'last_update' , 'date_joined','slug')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email' , 'password1', 'password2'),
        }),
    )
    add_form = UserAdminCreationsForm