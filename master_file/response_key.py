from rest_framework.response import Response
from rest_framework import status as ResponseStatus
from master_file import keys, messages
from django.http import HttpResponse

BAD_REQUEST = ResponseStatus.HTTP_400_BAD_REQUEST
FORBIDDEN = ResponseStatus.HTTP_403_FORBIDDEN

class TOKEN_EXPIRE(HttpResponse):
    def __init__(self):
        super().__init__('401 Token Expire', status=401)

class ACCOUNT_IS_INACTIVE(HttpResponse):
    def __init__(self):
        super().__init__(messages.ACCOUNT_IS_INACTIVE, status=403)

class INVALID_TOKEN(HttpResponse):
    def __init__(self):
        super().__init__(messages.INVALID_TOKEN, status=401)

def SIMPLE_ERROR_RESPONSE(msg=None):
    return Response({keys.SUCCESS:False, keys.MESSAGE:msg},status=BAD_REQUEST)

def SIMPLE_SUCCESS_RESPONSE(response={},header=None):
    if header:
        return Response({ keys.SUCCESS : True, keys.MESSAGE : messages.SUCCESS, **response}, headers=header)
    elif response:
        return Response({ keys.SUCCESS : True, keys.MESSAGE : messages.SUCCESS, **response})
    return Response({ keys.SUCCESS : True, keys.MESSAGE : messages.SUCCESS})

def SIMPLE_SUCCESS_RETURN(**response):
    return {keys.STATUS : True, **response}

def SIMPLE_ERROR_RETURN(msg=None,response=None,response_json={}):
    if msg:
        return {keys.STATUS : False, keys.ERROR : SIMPLE_ERROR_RESPONSE(msg,**response_json)}
    if response:
        return {keys.STATUS : False, keys.ERROR : response}
