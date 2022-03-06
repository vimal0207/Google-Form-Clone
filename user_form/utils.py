from user_form import models as user_form_model
from django.apps import apps
from master_file import keys
from helper import ModelHelper
from user_form import serializer as user_form_serializer

def user_form_instance(form_id):
    form = user_form_model.UserFormData.objects.get(id=form_id)
    form_name = form.form_name
    field_detail = form.filter_field
    options = {keys.VERBOSE_NAME: form_name, }
    model = ModelHelper.create_model(form_name, field_detail,
                                        options=options,
                                        admin_opts={},
                                        app_label=keys.USER_FORM,
                                        module='user_form',)
    model = apps.get_model(app_label=keys.USER_FORM, model_name=form_name)
    return model

def get_form_field_list(model):
    fields = model._meta.fields
    field_list = []
    for field in fields:
        if field.name not in [*keys.MASTER_EXCLUDE,keys.ID]:
            field_list.append(field.name)
    return field_list

def get_user_form_list(user):
    return user_form_model.UserFormData.objects.filter(user=user)

def get_form_serializer(model):
    serializer = user_form_serializer.master_serializer()
    serializer.Meta.model = model
    return serializer

def get_form_field_detail(request):
    form_id = request.GET.get(keys.FORM_ID, None)
    form = user_form_model.UserFormData.objects.get(id=form_id)
    if form.display_field:
        field_detail = form.display_field
        return field_detail
    model = request.model
    model_fields = model._meta.fields
    field_details = []
    for field in model_fields:
        field_detail = {}
        if field.name in [keys.ID, keys.DATA_ID, *keys.MASTER_EXCLUDE]:
            continue
        field_detail[keys.FIELD_NAME] = field.verbose_name
        field_detail[keys.FIELD_KEY] = field.name
        field_detail[keys.FIELD_MANDATORY] = True
        if field.null:
            field_detail[keys.FIELD_MANDATORY] = False
        field_type = field.get_internal_type()
        field_detail[keys.FIELD_TYPE] = keys.FIELD_TYPE_OBJECT[field_type]
        choices = field.choices
        if field.choices:
            field_detail[keys.FIELD_TYPE] = keys.SINGLE_SELECT_TYPE
            choices = [i[0] for i in choices]
        field_detail[keys.FIELD_OPTIONS] = choices
        field_details.append(field_detail)
    form.display_field = field_details
    form.save()
    return field_details

def get_model_data(request):
    id = request.GET.get(keys.ID)
    model = request.model
    filter_list = get_form_field_list(model)
    data = model.objects.all().order_by('id')
    if id:
        data = data.filter(**{keys.DATA_ID:id})
    if request.method == keys.DELETE:
        return data
    return list(data.values(*filter_list))

def get_data(request):
    instance = get_model_data(request)
    return instance[0]

def get_data_list(request):
    instance = get_model_data(request)
    return instance

def delete_data(request):
    instance = get_model_data(request)
    instance.delete()

def create_or_update_data(request):
    model = request.model
    request_data = request.data.copy()
    serializer = get_form_serializer(model)
    if request.method == keys.POST:
        data = get_model_data(request)
        if bool(data):
            data = data[-1]
            id = 1
            if data[keys.DATA_ID]:
                id = int(data[keys.DATA_ID]) + 1
        else:
            id = 1
        request_data[keys.DATA_ID] = id
        instance = serializer(data=request_data)
        if instance.is_valid():
            data = instance.save()
    else:
        id = request.GET.get(keys.ID)
        instance = model.objects.filter(**{keys.DATA_ID:id})
        data_dict = {}
        for key in request_data:
            data_dict[key] = request_data[key]
        instance.update(**data_dict)
    return {}