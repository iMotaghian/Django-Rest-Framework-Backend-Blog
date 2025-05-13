# [REST & API] https://en.wikipedia.org/wiki/REST / https://en.wikipedia.org/wiki/API & https://docs.github.com/en/rest?apiVersion=2022-11-28 / https://api.github.com/users/p30mehrdad

# [Django REST framework] installation (need add to requirements) -> https://www.django-rest-framework.org/
# install in docker
docker-compose exec backend sh
pip install djangorestframework
# Markdown support for the browsable API.
pip install markdown
# Filtering support    
pip install django-filter  

# Add 'rest_framework' to your INSTALLED_APPS setting.
INSTALLED_APPS = ['rest_framework',]

# sample:
from rest_framework.decorators import api_view
from rest_framework.response import Response
path('post/',views.api_post_list_view, name="api-post-list"),
# decorators:
@api_view()

# make new folder for api/v1 - link api to new folder in blog/urls.py - ( path('api/v1/', include('blog.api.url') )
# make blog/api/v1/urls.py

# [serializer] make object of model (DB) to json format - need make file or folder for serializers -> https://www.django-rest-framework.org/api-guide/serializers/
# code in api/v1/serializers.py also import serializers class in views.py

# [404] set 404 ER for not exist data with (try & except) and import status method (from rest_framework import status)
# [404] from django.shortcuts import get_object_or_404 and dont need to use (try & except)

# [ModelSerializer] import model to serializers.py and use in class inherited from ModelSerializer

# [POST serializer] make new post , need all date to set new post / in views ( @api_view(["GET","POST"]) )

# [PUT serializer] modify post / in views ( @api_view(["GET","PUT"]) )

# [DELETE serializer] in views ( @api_view(["GET","PUT","DELETE"]) )

# [Status Codes] -> https://httpstatuses.io/

# [postman app] send GET POST PUT DELETE request with this application (thunder client extension added to vscode like post man)

# [DRF Permissions] set in core/setting.py put (REST_FRAMEWORK), after need login OR set in views (IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser)-> https://www.django-rest-framework.org/ -> (APIs guide)
# if need login with api browsable need add a path in core/urls.py - path('api-auth/', include('rest_framework.urls')) -- in post man add authentication / Basic Auth

# [Class-based Views]-----------------------------------------------
# from rest_framework.views import APIView / class PostList(APIView) -> https://www.django-rest-framework.org/api-guide/views/
# change the urls path (views.PostList.as_view()) 
# permission_classes = [IsAuthenticated] # permissions for authenticated
# serializer_class = PostSerializer # convert json to from for POST method (html form)

# [Generic views] post list: need queryset / CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,...-> https://www.django-rest-framework.org/api-guide/generic-views
# [Generic views] post detail:need queryset / RetrieveUpdateDestroyAPIView ->  https://www.django-rest-framework.org/api-guide/generic-views

# [ViewSet] in url set function name - "as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})" - "def list(self, request):" all name : list,create,retrieve,update,partial_update,destroy -> https://www.django-rest-framework.org/api-guide/viewsets
# 6-9 [viewsets.ModelViewSet] all task in ViewSet is do by ModelViewSet with lowest code
# [DefaultRouter] in urls.py >>  from rest_framework.routers import DefaultRouter ... / "urlpatterns = router.urls" or "path('',include(router.urls))" or "urlpatterns += router.urls"
# [Routers] SimpleRouter and DefaultRouter (with api-root) >> urlpatterns += router.urls / path('', include(router.urls)),   -> https://www.django-rest-framework.org/api-guide/routers/
# [@action] extra action in view set >> from rest_framework.decorators import action & @action(methods=["get"],detail=False) >> default method is get >> if need pk "detail=True" or not "detail=False" >> and "url_path" , "url_name" ... -> https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing

# 6-11 [api mini documentation] coreapi ->> watch again 6-11

# 6-12 [ReadOnlyField] in serializer : content = serializers.ReadOnlyField() or serializers.CharField(read_only=True) or in meta: read_only_fields = ['content'] -> cant change this filed in api (put patch) -> https://www.django-rest-framework.org/api-guide/fields/#readonlyfield
# 6-13 [make new filed in serializer] for example make "snippet" field in PostSerializer and make function (get_snippet) for "snippet" in related model and in serializer.py snippet = serializers.ReadOnlyField(source='get_snippet')
# [get_absolute_url] make relative_url for each post and show in api - in models : get_absolute_api_url() and in serializer : relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True) --> "relative_url": "/blog/api/v1/post/20/",
# 6-14 [serializer method] in serializer :absolute_url = serializers.SerializerMethodField() / function name is : get_absolute_url  -> https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
# 6-15 [relations] SlugRelatedField: send data of many to many or forgin key relation of model (send name of field . not only id) example "category" //// category = CategorySerializer() -- has bug . use to_representation() -> https://www.django-rest-framework.org/api-guide/relations/#slugrelatedfield
# 6-16 [to_representation()] in serializer we can make export of api specially for each field // automatic is added to json export [get]
# 6-17 [seprate List (object.all()) and a Object (object.get(...))] user request in function in serializer : request = self.context.get('request') /// if request.parser_context.get('kwargs').get('pk'):
# 6-18 [create post with out select user (import from login user)] need set 'create' function in serializer, also set 'user' as read only: def create(self, validated_data): in serializer
# 6-19 [Permissions] make permissions.py in api folder (from rest_framework import permissions) / permissions.BasePermission -> https://www.django-rest-framework.org/api-guide/permissions/
# 6-20 [Filtering] DjangoFilterBackend: pip install django-filter / add to setting INSTALLED_APPS 'django_filters', / from django_filters.rest_framework import DjangoFilterBackend -> https://www.django-rest-framework.org/api-guide/filtering/
# 6-21 [SearchFilter] from rest_framework import filters / filter_backends = / search_fields = -> https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
# 6-22 [OrderingFilter] filter_backends = [filters.OrderingFilter] / ordering_fields = ['username', 'email'] -> https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
# 6-23 [Pagination] make paginations.py / from rest_framework.pagination import PageNumberPagination //// Custom pagination styles / def get_paginated_response -> https://www.django-rest-framework.org/api-guide/pagination/
# 6-24 [more filters] 24-فیلترهای بیشتر.docx





