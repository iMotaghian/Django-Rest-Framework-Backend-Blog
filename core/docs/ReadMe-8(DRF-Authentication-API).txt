# 8-1 [Accounting API] first make 'urls.py' in "accounts" folder & make "api" folder in "accounts" folder and ...
# edit rout of accounts in core/urls.py "include("accounts.urls")" and after add new rout to accounts/urls.py for accounting rout -> path("", include("django.contrib.auth.urls")),
# 8-2 [Djoser information] -> https://djoser.readthedocs.io/en/latest/  & https://django-rest-auth.readthedocs.io/en/latest/
# 8-3 [API auth URLS] in urls.py : app_name = 'api-v1' ////  registration, change password, reset password, login token and login jwt // edit view and serializers 
# 8-4 [Registration Endpoint] need password1, password2, email for Registration and password1,password2 must be equal together (check with "validate" function in serializer)  -> https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html#registration
# also we must check password pattern in "validate" function

# 8-5 [Token Authentication - login] add to INSTALLED_APPS : 'rest_framework.authtoken' in settings -> https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
# after settings need migration because token data insert to DB (in admin panel -> Tokens) :
docker-compose exec backend sh
python manage.py migrate
# add REST_FRAMEWORK in settings.py  //// 'rest_framework.authentication.TokenAuthentication',
# can use token in "Modheader" extension in browser (temporary) -> Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

# 8-6 [login - ObtainAuthToken] add from "from rest_framework.authtoken.views import ObtainAuthToken" to api urls -> https://www.django-rest-framework.org/api-guide/authentication/#by-exposing-an-api-endpoint
# 8-7 [custom login] use 'ObtainAuthToken' in views.py for make custom class for login /// class CustomObtainAuthToken(ObtainAuthToken) - also make CustomAuthTokenSerializer in serializer.py
# 8-8 [custom logout] delete token of user : use "from rest_framework.views import APIView" in views.py /// class CustomDiscardAuthToken(APIView)

# 8-9 [Jason Web Token] -> https://jwt.io/

# 8-10 [SimpleJWT] Requirements -> https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
docker-compose exec backend sh
pip install djangorestframework-simplejwt
# add to settings.py in REST_FRAMEWORK - 'rest_framework_simplejwt.authentication.JWTAuthentication', /// INSTALLED_APPS  - 'rest_framework_simplejwt',
# make urls.py : from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView--> for check token validated 

# 8-11 [JWT in Postman] for jwt-login put access token in get list -> Auth Type : Bearer Token
# 8-12 [Custom JWT] make CustomTokenObtainPairView in views.py and import TokenObtainPairView also make CustomTokenObtainPairSerializer for this class // def validate(self, attrs) in serializers.py
# 8-13 [SimpleJWT setting] Django project settings.py // SIMPLE_JWT -> https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
# 8-14 [UserVerification] -> https://github.com/AliBigdeli/Django-CustomUser-DRF-App/tree/with-verification
# [Change Password] class ChangePasswordApiView in views.py and ChangePasswordSerializer in serializers.py
# 8-15 [Profile Endpoint] in views.py : ProfileApiView and in serializers.py ProfileSerializer -- urls.py : path('profile/',views.ProfileApiView.as_view(),name='profile')
# 8-16 [Optimize accounts models] make folder "models" in "accounts" folder and make users.py & profiles.py // update __init__.py "from .users import *" & "from .profiles import *"
# [Optimize accounts urls] in "v1" make 'urls' folder and ... and update __init__.py

# 8-17 [User verification] add "is_verified" field to User model (default is false except superuser is true) also add 'is_verified' field in admin.py
docker-compose exec backend sh
python manage.py makemigrations
python manage.py migrate
# add validated in "CustomAuthTokenSerializer" for user validate and other class that needed.

# 8-18 [User Activation] need token need send email read more in '8-23' // path('activation/confirm/'), // path('activation/resend/'),

# 8-19 [Django mail] urls.py "path('test-email',views.TestEmailSend.as_view(),name='test-email')" & views.py "TestEmailSend" /// add in setting.py "EMAIL_BACKEND" -> https://docs.djangoproject.com/en/5.2/topics/email/
# 8-20 [SMTP4DEV in Docker] update docker-compose.yml : smtp4dev -> https://github.com/rnwood/smtp4dev/wiki/Installation#how-to-run-smtp4dev-in-docker & https://github.com/rnwood/smtp4dev/blob/master/docker-compose.yml
# address smtp4dev service http://127.0.0.1:5000/ // config -> https://github.com/rnwood/smtp4dev/wiki/Configuring-Clients
# set smtp4dev mail config in settings.py , EMAIL_BACKEND ...
# 8-21 [email template] django-mail-templated /// update Requirements.txt  // -> https://django-mail-templated.readthedocs.io/en/master/
docker-compose exec backend sh
pip install django-mail-templated
# add 'mail_templated' to "INSTALLED_APPS" in settings.py
# use "from mail_templated import send_mail" in views.py and "send_mail('email/hello.tpl', {'name': 'ali'}, 'admin@admin.com', ['mehrdad@gmail.com'])" in mail class
# make folder in 'templates' as 'email' and make 'hello.tpl' on this
# more info -> https://django-mail-templated.readthedocs.io/en/master/advanced_usage.html
# 8-22 [Threading email] make 'utils.py' in api folder for processing our mail data, make python Threading class in utils (class EmailThread) , import "EmailThread" in views.py

# 8-23 [manual token generation] use "from rest_framework_simplejwt.tokens import RefreshToken" in views.py // add "RefreshToken" in mail class  -> https://django-rest-framework-simplejwt.readthedocs.io/en/latest/creating_tokens_manually.html
# 8-24 [active user with token] use get_tokens_for_user() in Registration class in view / and make url 'activation/confirm/<str:token>' and class "ActivationApiView" for it
# 8-25 [ActivationApiView()] need decode jwt token and get user id for activation and after in make "Ture" is_verified
# [ActivationResendApiView] resend Activation link : path('activation/resend/',views.ActivationResendApiView.as_view(), name='activation-resend')
# 8-26 [ActivationResendApiView serializer]
# reset password ?
# 8-27 [update version of APIs] for example install djoser for v2 of api -> https://djoser.readthedocs.io/en/latest/getting_started.html
docker-compose exec backend sh
pip install -U djoser
# INSTALLED_APPS add 'djoser', //// add "path('api/v2/', include('djoser.urls'))," and "path('api/v2/', include('djoser.urls.jwt'))," to api "urlpatterns" in accounts/urls.py













