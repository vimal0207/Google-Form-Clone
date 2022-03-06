from django.urls import path
from user_form import views as user_form_views

urlpatterns = [
    path('api/create_form/',user_form_views.create_form,name="create_form"),
    path('api/form_list/',user_form_views.get_form_list,name="form_list"),
    path('form_field/',user_form_views.get_form_field,name="form_field"),
    path('form_data/',user_form_views.form_data,name="form_data"),
    path('api/form_data_list/',user_form_views.form_data_list,name="form_data_list"),
]