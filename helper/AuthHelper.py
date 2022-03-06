import jwt
from master_file import keys, response_key
from datetime import datetime, timedelta
from pillarplus import settings

def get_token(user):
    token_payload = {
        keys.USER_ID : user.id,
        keys.IAT : datetime.now(),
        keys.EXP : datetime.now() + timedelta(days=int(settings.TOKEN_TIMELINE))
    }
    return str(jwt.encode(token_payload, settings.JWT_SECRET, algorithm=keys.HS256).decode())

def get_refresh_token(user):
    token_payload = {
        keys.USER_ID : user.id,
        keys.IAT : datetime.now(),
        keys.EXP : datetime.now() + timedelta(days=int(settings.REFRESH_TOKEN_TIMELINE))
    }
    return str(jwt.encode(token_payload, settings.JWT_SECRET, algorithm=keys.HS256).decode())

def generate_token(user,token_type=keys.TOKEN):
    """
    method to make access_token(jwt) from user table ID
    :param user_id:  Non null/valid user table ID
    :return: token, refresh_token
    """
    response_json = {}
    response_json[keys.TOKEN] = get_token(user)
    if token_type == keys.BOTH:
        response_json[keys.REFRESH_TOKEN] = get_refresh_token(user)
    return response_json

def decode_token(token):
    jwt_secret = settings.JWT_SECRET
    return jwt.decode(token, jwt_secret, algorithm=keys.HS256)

def check_token_validity(request):
    try:
        if request.META.get(keys.HTTP_REFRESH_TOKEN, None):
            token = request.META.get(keys.HTTP_REFRESH_TOKEN, None)
        else:
            token = request.META.get(keys.HTTP_TOKEN, None)
        token = decode_token(token)
        expiry_date = datetime.fromtimestamp(token[keys.EXP] / 1e3)
        if datetime.now() > expiry_date:
            return response_key.SIMPLE_SUCCESS_RETURN()
    except Exception as e:
        pass
    return response_key.SIMPLE_ERROR_RETURN(response=response_key.TOKEN_EXPIRE())

def validate_token(request):
    from user import utils as user_utils
    try:
        response = check_token_validity(request)
        if not response[keys.STATUS]:
            return response
        if request.META.get(keys.HTTP_REFRESH_TOKEN, None):
            token = request.META.get(keys.HTTP_REFRESH_TOKEN, None)
        else:
            token = request.META.get(keys.HTTP_TOKEN, None)
        if bool(token):
            user_id = decode_token(token)[keys.USER_ID]
            user_instance = user_utils.get_user(request,id=user_id)
            if user_instance.is_active:
                return response_key.SIMPLE_SUCCESS_RETURN(**{keys.INSTANCE: user_instance})
            else:
                return response_key.SIMPLE_ERROR_RETURN(response=response_key.ACCOUNT_IS_INACTIVE())
        return response_key.SIMPLE_ERROR_RETURN(response=response_key.INVALID_TOKEN())
    except Exception as e:
        return response_key.SIMPLE_ERROR_RETURN(msg=str(e))