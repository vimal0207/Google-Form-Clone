from drf_yasg import openapi
from master_file import keys


# **********************HEADER*****************************

HEADER_TOKEN = openapi.Parameter(keys.TOKEN, openapi.IN_HEADER,
                                 description="ex-eyJ0eXA......",
                                 type=openapi.TYPE_STRING,
                                 required=True)

HEADER_REFRESH_TOKEN = openapi.Parameter(keys.REFRESH_TOKEN, openapi.IN_HEADER,
                                         description="ex-eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.....",
                                         type=openapi.TYPE_STRING,
                                         required=True)

# ***********************PARAMS**********************************

EMAIL = openapi.Parameter(keys.EMAIL, openapi.IN_QUERY,
                                   description="vm@gmail.com",
                                   type=openapi.TYPE_STRING,
                                   required=True)

PASSWORD = openapi.Parameter(keys.PASSWORD, openapi.IN_QUERY,
                                   description="************",
                                   type=openapi.TYPE_STRING,
                                   required=True)


FORM_ID = openapi.Parameter(keys.FORM_ID, openapi.IN_QUERY,
                                   description="EX: 1",
                                   type=openapi.TYPE_INTEGER,
                                   required=True)

ID = openapi.Parameter(keys.ID, openapi.IN_QUERY,
                            description="EX: 1",
                            type=openapi.TYPE_INTEGER,
                            required=True)
