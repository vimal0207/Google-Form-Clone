from rest_framework import serializers
from user import models as user_models
from user_form import models as user_form_models
from master_file import keys

class CreateAccountPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = [keys.EMAIL, keys.PASSWORD]

class UserFormDataPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_form_models.UserFormData
        exclude = keys.MASTER_EXCLUDE + [keys.FILTER_FIELD, keys.DISPLAY_FIELD, keys.IS_FORM_CREATED, keys.USER]