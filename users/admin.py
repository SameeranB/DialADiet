from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('On-boarding Status'), {'fields': ('personal_info_complete', 'family_medical_history_complete', 'personal_medical_history_complete', 'associated_health_problems_complete', 'daily_routine_complete',  'on_boarding_complete', 'payment_complete')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'on_boarding_complete', 'payment_complete')
    list_filter = ('is_staff', 'on_boarding_complete', 'payment_complete')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


