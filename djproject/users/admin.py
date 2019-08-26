from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin """
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff') 

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            )
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Meñtadata', {
            'fields': (('created', 'modified'))
        })
    )

    readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
