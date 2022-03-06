from django.contrib import admin
from user_form import models as user_form_models

@admin.register(user_form_models.UserFormData)
class UserFormDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'form_name', 'created','modified')
    search_fields = ["id", "form_name"]
