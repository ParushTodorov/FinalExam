from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from final_exam_project.accounts.forms import UserCreateForm, UserChangeForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    list_display = ("username", "email", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "email", "is_staff")
    ordering = ("username", "is_active", "is_staff")

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'password',
                    'email',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'age',
                    'city',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                ),
            },
        ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'age')}
         ),
    )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         # edit mode... add fields here to make them read-only when editing
    #         return self.readonly_fields
    #     else:
    #         self.inlines = []
    #         return self.readonly_fields

