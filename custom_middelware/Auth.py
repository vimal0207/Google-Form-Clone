from helper import AuthHelper
from master_file import keys
from user_form import utils as user_form_utils

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        url = request.build_absolute_uri()
        if keys.FORM_ID in request.GET:
            form_id = request.GET.get(keys.FORM_ID)
            request.model = user_form_utils.user_form_instance(form_id)
        if '/api/' in url:
            response = AuthHelper.validate_token(request)
            if not response[keys.STATUS]:
                return response[keys.ERROR]
            request.user = response[keys.INSTANCE]
        response = self.get_response(request)
        return response
