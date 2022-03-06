from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from master_file import open_api_serializers, keys, open_api_keys, messages, response_key
from user_form import utils as user_form_utils
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from user_form import serializer as user_form_serializer

@swagger_auto_schema(
    method="post", request_body=open_api_serializers.UserFormDataPOSTSerializer, manual_parameters=[open_api_keys.HEADER_TOKEN])
@csrf_exempt
@api_view(["POST"])
@parser_classes([MultiPartParser])
def create_form(request):
    response_json = {}
    user = request.user
    request_data = request.data.copy()
    request_data[keys.USER] = user.id
    serializer = user_form_serializer.UserFormDataSerializer(data = request_data)
    if serializer.is_valid():
        serializer.save()
        response_json[keys.FORM_DETAIL] = serializer.data
        return response_key.SIMPLE_SUCCESS_RESPONSE(response=response_json)
    else:
        return response_key.SIMPLE_ERROR_RESPONSE(msg=serializer.errors)

@swagger_auto_schema(
    method="get", manual_parameters=[open_api_keys.HEADER_TOKEN])
@api_view(["GET"])
def get_form_list(request):
    user = request.user
    response_json = {}
    form_list = user_form_utils.get_user_form_list(user)
    form_list = user_form_serializer.UserFormDataSerializer(form_list, many=True).data
    response_json[keys.FORM_LIST] = form_list
    return response_key.SIMPLE_SUCCESS_RESPONSE(response=response_json)

@swagger_auto_schema(
    method="get", manual_parameters=[open_api_keys.FORM_ID])
@api_view(["GET"])
def get_form_field(request):
    response_json = {}
    form_id = request.GET.get(keys.FORM_ID, None)
    if  not form_id:
        return response_key.SIMPLE_ERROR_RESPONSE(msg = messages.INALID_ID)
    form_field = user_form_utils.get_form_field_detail(request)
    response_json[keys.FORM_FIELD_DETAIL] = form_field
    return response_key.SIMPLE_SUCCESS_RESPONSE(response=response_json)

@swagger_auto_schema(
    method="get", manual_parameters=[open_api_keys.HEADER_TOKEN,open_api_keys.FORM_ID])
@api_view(["GET"])
def form_data_list(request):
    response_json = {}
    if not request.GET.get(keys.FORM_ID, None):
        return response_key.SIMPLE_ERROR_RESPONSE(msg = messages.FORM_ID)
    form_data = user_form_utils.get_data_list(request)
    response_json[keys.FORM_DATA_LIST] = form_data
    return response_key.SIMPLE_SUCCESS_RESPONSE(response=response_json)

@swagger_auto_schema(
    method="get", manual_parameters=[open_api_keys.FORM_ID, open_api_keys.ID])
@swagger_auto_schema(
    method="post", manual_parameters=[open_api_keys.FORM_ID])
@swagger_auto_schema(
    method="patch", manual_parameters=[open_api_keys.FORM_ID, open_api_keys.ID])
@swagger_auto_schema(
    method="delete", manual_parameters=[open_api_keys.FORM_ID, open_api_keys.ID])
@api_view(["GET","POST","PATCH","DELETE"])
def form_data(request):
    response_json = {}
    if  not request.GET.get(keys.FORM_ID, None):
        return response_key.SIMPLE_ERROR_RESPONSE(msg = messages.FORM_ID)
    if request.method in [keys.GET, keys.DELETE, keys.PATCH]:
        if not request.GET.get(keys.ID, None):
            return response_key.SIMPLE_ERROR_RESPONSE(msg = messages.INALID_ID)
        if request.method == keys.GET:
            form_data = user_form_utils.get_data(request)
        elif request.method == keys.PATCH:
            form_data = user_form_utils.create_or_update_data(request)
        else:
            form_data = user_form_utils.delete_data(request)

        response_json[keys.FORM_DATA] = form_data
    else:
        form_data = user_form_utils.create_or_update_data(request)
    return response_key.SIMPLE_SUCCESS_RESPONSE(response=response_json)