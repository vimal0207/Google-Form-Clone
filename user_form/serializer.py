from rest_framework import serializers
from user_form import models as user_form_models
from master_file import keys

class UserFormDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_form_models.UserFormData
        exclude = keys.MASTER_EXCLUDE + [keys.FILTER_FIELD, keys.DISPLAY_FIELD, keys.IS_FORM_CREATED]

def master_serializer():
    class MasterSerializer(serializers.ModelSerializer):

        class Meta:
            model = None
            exclude = keys.MASTER_EXCLUDE
    
    return MasterSerializer