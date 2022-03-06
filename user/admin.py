from django.contrib import admin
from user import models as user_models

@admin.register(user_models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created','modified')
    search_fields = ["id", "email"]
