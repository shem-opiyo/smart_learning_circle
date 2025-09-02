from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, EducatorProfile, StudentProfile, LearningCircle, ChatMessage, Payment

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(EducatorProfile)
admin.site.register(StudentProfile)
admin.site.register(LearningCircle)
admin.site.register(ChatMessage)
admin.site.register(Payment)
