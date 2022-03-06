from django.db.models.signals import post_save
from django.dispatch import receiver
from user_form import models as user_form_models
import pandas as pd
from pillarplus import settings
from master_file import keys
from django.db import models
from helper import ModelHelper
from django.apps import apps


@receiver(post_save, sender=user_form_models.UserFormData)
def form_signal(sender, instance, created, **kwargs):
    if created:
        form_name = instance.form_name
        url = instance.file.url
        if settings.SERVER_URL:
            url = f'{settings.SERVER_URL}{url}'
        file=pd.read_csv(url,encoding= "unicode_escape")
        file = file.fillna(False)
        file_len = len(file)
        field_detail = {}
        for i in range(file_len):
            real_name = file.iloc[i][keys.FIELD_NAME]
            field_name = str(real_name).replace(' ','_')
            field_type = str(file.iloc[i][keys.FIELD_TYPE])
            options = file.iloc[i][keys.FIELD_OPTIONS]
            field_options = []
            if options:
                options = str(options).split(',')
                for option in options:
                    field_options.append([option,option])
            mandatory = str(file.iloc[i][keys.FIELD_MANDATORY]).lower()
            field_mandatory = False
            if mandatory == keys.FIELD_FALSE:
                field_mandatory = True
            field_rule = {}
            field_rule[keys.BLANK] = field_mandatory
            field_rule[keys.NULL] = field_mandatory
            field_rule[keys.DB_COLUMN] = real_name
            if field_type == keys.NUMBER_TYPE:
                field_detail[field_name] = models.IntegerField(**field_rule)
            elif field_type == keys.DATE_TYPE:
                field_detail[field_name] = models.DateField(**field_rule)
            else:
                field_rule[keys.MAX_LENGTH] = 200
                if len(field_options):
                    field_rule[keys.FIELD_CHOICES] = field_options
                field_detail[field_name] = models.CharField(**field_rule)
        field_detail[keys.CREATED] = models.DateTimeField(auto_now=False, auto_now_add=True)
        field_detail[keys.MODIFIED] = models.DateTimeField(auto_now=True, auto_now_add=False)
        field_detail[keys.DATA_ID] = models.BigIntegerField()
        ModelHelper.create_table(form_name, field_detail, keys.USER_FORM)
        instance.filter_field = field_detail
        instance.is_form_created = True
        instance.save()