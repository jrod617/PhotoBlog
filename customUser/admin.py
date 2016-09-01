""" Admin definition for ChasinViewsUser """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import ChasinViewsUserChangeForm, ChasinViewsUserCreationForm
from .models import ChasinViewsUser


class ChasinViewsUserAdmin(UserAdmin):

    """ ChasinViewsUser Admin model """

    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        (_('Personal info'), {'fields': ('birth_date', 'gender', 'state', 'city', 'countryOfOrigin',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2')
        }
    ),
    )

    # The forms to add and change user instances
    form = ChasinViewsUserChangeForm
    add_form = ChasinViewsUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username','email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# Register the new ChasinViewsUserAdmin
admin.site.register(ChasinViewsUser, ChasinViewsUserAdmin)