from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from master_file import open_api_serializers, keys, open_api_keys, messages, response_key
from helper import Helper, AuthHelper
from user import utils as user_utils

@swagger_auto_schema(
    method="post", request_body=open_api_serializers.CreateAccountPOSTSerializer)
@csrf_exempt
@api_view(["POST"])
def create_user(request):
    request_data = request.data.copy()
    user_email = str(request_data[keys.EMAIL]).lower()
    if user_utils.is_user_available(email=user_email):
        return response_key.SIMPLE_ERROR_RESPONSE(messages.USER_ALREADY)
    user = user_utils.create_account(request_data)
    token = AuthHelper.generate_token(user=user,token_type=keys.BOTH)
    return response_key.SIMPLE_SUCCESS_RESPONSE(header=token)

@swagger_auto_schema(
    method="get", manual_parameters=[open_api_keys.EMAIL,open_api_keys.PASSWORD]
)
@api_view(['GET'])
def verify_login(request):
    request_data= request.GET
    user = user_utils.verify_login(request_data)
    if not user:
        return response_key.SIMPLE_ERROR_RESPONSE(msg=messages.INVALID_TOKEN)
    token = AuthHelper.generate_token(user=user,token_type=keys.BOTH)
    return response_key.SIMPLE_SUCCESS_RESPONSE(header=token)

@swagger_auto_schema(method='get', manual_parameters=[open_api_keys.HEADER_REFRESH_TOKEN])
@api_view(['GET'])
def refresh_token(request):
    user = request.user
    token = user_utils.get_user_token(user)
    return response_key.SIMPLE_SUCCESS_RESPONSE(header=token)