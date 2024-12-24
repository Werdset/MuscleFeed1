from django.contrib import admin
from .models import Profile, EmailVerification, ResetPasswordVerification, ChangePersonalDataRequest

# Админка для модели Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'phone', 'main_address', 'created', 'get_other_addresses')
    search_fields = ('user__username', 'name', 'surname', 'phone')
    list_filter = ('created', 'user__is_active', 'user__is_staff')
    ordering = ('-created',)
    readonly_fields = ('user', 'created')
    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'surname', 'phone', 'main_address', 'other_addresses')
        }),
        ('Дополнительная информация', {
            'fields': ('created',)
        }),
    )

    def get_other_addresses(self, obj):
        return ", ".join(obj.get_other_addresses())
    get_other_addresses.short_description = 'Другие адреса'

# Админка для модели EmailVerification
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'new_email', 'key', 'created')
    search_fields = ('user__username', 'new_email')
    list_filter = ('created',)
    ordering = ('-created',)

# Админка для модели ResetPasswordVerification
class ResetPasswordVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created')
    search_fields = ('user__username',)
    list_filter = ('created',)
    ordering = ('-created',)

# Админка для модели ChangePersonalDataRequest
class ChangePersonalDataRequestAdmin(admin.ModelAdmin):
    list_display = ('profile', 'type', 'new', 'done', 'created')
    search_fields = ('profile__user__username', 'new')
    list_filter = ('done', 'type', 'created')
    ordering = ('-created',)

    def save_model(self, request, obj, form, change):
        if obj.done:
            setattr(obj.profile, obj.type, obj.new)
            obj.profile.save()
        super().save_model(request, obj, form, change)

# Регистрация моделей в админке
admin.site.register(Profile, ProfileAdmin)
admin.site.register(EmailVerification, EmailVerificationAdmin)
admin.site.register(ResetPasswordVerification, ResetPasswordVerificationAdmin)
admin.site.register(ChangePersonalDataRequest, ChangePersonalDataRequestAdmin)