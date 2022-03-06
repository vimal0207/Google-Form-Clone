from django.db import models
from user import models as user_models
from picklefield.fields import PickledObjectField

class UserFormData(models.Model):
    form_name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(to=user_models.User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='form/file')
    is_form_created = models.BooleanField(default = False)
    filter_field = PickledObjectField(null=True, blank=True)
    display_field = PickledObjectField(null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"