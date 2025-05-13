# 16-1 [Cache] save in Memory for unusable data -> https://docs.djangoproject.com/en/5.2/topics/cache/

# 16-2 [Cache Backends] Memcached - Redis - Database caching - Filesystem caching - Local-memory caching - Dummy caching (for development) -> https://docs.djangoproject.com/en/5.2/topics/cache/#setting-up-the-cache

# 16-3 [Postman Mock server] in postman > create mock server > new collection > server name > request url (/test/delay/5)> response body > no env > simulate > save mock server > create
# get server url (url request) > https://bd5a0fc4-e2b9-4dda-be77-c569b41ac786.mock.pstmn.io/test/delay/5
# make endpoint > accounts/urls.py > path("test/", views.test, name="test"), -> http://127.0.0.1:8000/accounts/test/

# 16-4 [Django Redis caching] Transport -> https://pypi.org/project/django-redis/3.1.6/ & https://github.com/jazzband/django-redis
docker-compose exec backend sh
pip install django-redis
exit
docker-compose exec worker sh
pip install django-redis
# for setup add "CACHES =" to setting.py

# 16-5 [django caching] in accounts/view.py > from django.core.cache import cache -> https://docs.djangoproject.com/en/5.2/topics/cache/#basic-usage
# cache.get() /// cache.set()

# 16-6 [redis keys of cache] check cache saved, go to redis shell:
redis-cli
# select "LOCATION": "redis://redis:6379/2", for caching:
select 2 
# list of all keys cache:
keys * 
## 1) ":1:test_delay_api"
get ":1:test_delay_api"
## "\x80\x04\x95[\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\bmesseage\x94\x8c\x0ethis is a test\x94\x8c\x04date\x94\x8c\x182025-04-28T12:58:31.026Z\x94\x8c\x06number\x94\x8c\x0c685-411-7875\x94u."

# [Decorator Cache] The per-view cache -> https://docs.djangoproject.com/en/5.2/topics/cache/#the-per-view-cache
# use "from django.views.decorators.cache import cache_page" in accounts/views
redis-cli
select 2 
keys *
## 1) ":1:views.decorators.cache.cache_page..GET.e5304c50a3fee29ff2cccd656f3129ed.d41d8cd98f00b204e9800998ecf8427e.en-us.UTC"
## 2) ":1:views.decorators.cache.cache_header..e5304c50a3fee29ff2cccd656f3129ed.en-us.UTC"





