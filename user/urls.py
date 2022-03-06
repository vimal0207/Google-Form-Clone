from django.urls import path
from user import views as user_views

urlpatterns = [
    path('singup/',user_views.create_user,name="singup"),
    path('singin/',user_views.verify_login,name="singin"),
    path('api/refresh_token/',user_views.refresh_token,name="refresh_token"),
]