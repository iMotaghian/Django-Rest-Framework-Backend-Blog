# 7-1 [Documenting your API] generate API to API doc "swagger" -> https://github.com/axnsan12/drf-yasg/ /// pip install --upgrade drf-yasg[validation] -> https://www.django-rest-framework.org/topics/documenting-your-api/ /// (more plugin: redoc - insomnia)
# add 'drf_yasg', to INSTALLED_APPS and after edit core/urls.py
# address: http://127.0.0.1:8000/swagger/ and http://127.0.0.1:8000/redoc/

# 7-2 [swagger.json] path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'), -> http://127.0.0.1:8000/swagger.json/
# can download swagger.json and import to 'postman' and get all date of api in postman automatically


























