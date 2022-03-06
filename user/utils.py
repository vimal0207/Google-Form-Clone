from user import models as user_models
from master_file import keys

def is_user_available(email):
    email = str(email).lower()
    if user_models.User.objects.filter(**{keys.EMAIL:email}).exists():
        return True
    return False 

def verify_login(request_data):
    email = request_data[keys.EMAIL]
    if user_models.User.objects.filter(**{keys.EMAIL:email}).exists():
        password = request_data[keys.PASSWORD]
        user = user_models.User.objects.get(**{keys.EMAIL:email})
        if user.check_password(password):
            return user
    return False

def create_account(request_data):
    add_dict = {}
    add_dict[keys.EMAIL] = str(request_data[keys.EMAIL]).lower()
    add_dict[keys.USER_NAME] = add_dict[keys.EMAIL]
    instance = user_models.User.objects.create(**add_dict)
    instance.set_password(request_data[keys.PASSWORD])
    instance.save()
    return instance

def get_user(request,id=None):
    return user_models.User.objects.get(id=id)
