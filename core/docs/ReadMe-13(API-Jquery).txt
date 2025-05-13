# 13-1 [APIView] path("post/api/", views.PostListApiView.as_view(), name="post-list-api"), in blog urls.py 
# add PostListApiView in blog view (template_name = "blog/post_list_api.html")

# 13-2 [CORS policy] A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins
# https://pypi.org/project/django-cors-headers/
docker-compose exec backend sh
python -m pip install django-cors-headers
# add it to your installed apps: INSTALLED_APPS = ["corsheaders",]
# add to settings: MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware", "django.middleware.common.CommonMiddleware",]
# add to settings: CORS_ALLOWED_ORIGINS = ["https://example.com",]
# full access: CORS_ALLOW_ALL_ORIGINS = True



