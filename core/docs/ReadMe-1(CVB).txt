
# [GIT] initialize repository
# make barnch main
git init -b main
git status
# add all file to git (in django app folder)
git add .
# set frist commit
git commit -m "initial commit"

# [Django]
pip install django
pip freeze > requirements.txt

# [Django]
django-admin startproject core

# [Dockerfile] make docker
# [docker compose] make docker compose

# [control environment variables] / we can use https://pypi.org/project/python-decouple/
pip install python-decouple
# in core/settings.py add -> https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html
from decouple import config
# and edit
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')], default="*")
# after update docker-compose.yml file (add new environment)

# [https://dbdiagram.io/]

# [installing apps] accounts & blog (if docker-compose is run) 
docker-compose exec backend sh
python manage.py startapp accounts
python manage.py startapp blog
# add to project -> core/settings.py / INSTALLED_APPS

# [Blog models] create Post models in blog/models.py -> https://dbdiagram.io/d/menu9-67c78ede263d6cf9a03b0a11

# [Accounting models] create Account models in accounts/models.py / use custom User models (AbstractUser vs AbstractBaseUser) -> https://testdriven.io/blog/django-custom-user-model/
# add models to django / go to settings and (# user manager config) / in setting : AUTH_USER_MODEL = 'accounts.User'

# [exec] in docker and set migrations /
docker compose exec backend sh
python manage.py makemigrations
python manage.py migrate
# and create super user
python manage.py createsuperuser
# admin@admin.com admin

# set models for admin / go accounts/admin.py (new verison)

# profile models in accounts/models.py

# [SIGNAL] create new profle after create a new user / make in accounts/models.py (post_save) -> https://docs.djangoproject.com/en/5.1/topics/signals/ -> https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html

# set static directory for save files
# go to core/settings.py and add STATICFILES_DIRS, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
# after go to core/urls.py (serving static and media for development)

# migrate blog DB and go to blog/admin.py add db
 
# [class base views] -> https://docs.djangoproject.com/en/5.1/topics/class-based-views/

# update core/urls.py and make urls.py in blog folder

# make templates folder and set in core/settings.py -> TEMPLATES -> 'DIRS': [BASE_DIR / 'templates',]

# [templateview] code in blog/views.py & urls.py
# [redirectview] code in blog/urls.py
# [listview] code in blog/views.py (model=Post) and urls.py / need make folder in templates folder as app name (blog) and make html file as path name (post_list.html) / in html get data form model in "object_list" -> {% for post in object_list %}
# [listview] or change name in "object_list" with context_object_name in views.py -> https://docs.djangoproject.com/en/5.1/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin
# [listview] pagination views.py : (paginate_by = 2) & (/blog/post/?page=2) -> https://docs.djangoproject.com/en/5.1/topics/pagination/
# [listview] ordering views.py : (ordering ='-id')
# [DetailView] show Detail data like list view work with ID - create templateS/blog/post_detail.html - default return object in html (object) -> https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/
# [FormView] create forms.py in blog dir and make url in blog/urls.py (name="post-create-view") and contact.html-> https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView
# [CreateView] like FormView but most loaded model in class also need template (blog/post_form.html) - with form_valid user can login and send post -> https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-editing/
# [UpdateView] urls.py & views.py (PostEditView) - template (blog/post_form.html)  -> https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-editing/#django.views.generic.edit.UpdateView 
# [DeleteView] urls.py & views.py (PostDeleteView) - template (blog/post_confirm_delete.html) -> https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-editing/#django.views.generic.edit.DeleteView

# [Django authentication URLs] need add core/urls.py - path("accounts/", include("django.contrib.auth.urls")), -> https://docs.djangoproject.com/en/5.1/topics/auth/default/#module-django.contrib.auth.views
# [LoginRequiredMixin] for login user add LoginRequiredMixin (first) to any class that needed  (from django.contrib.auth.mixins import LoginRequiredMixin) -> https://docs.djangoproject.com/en/5.1/topics/auth/default/
# [PermissionRequiredMixin] add PermissionRequiredMixin to class view and set " permission_required =" for users

# migrated from user in post models to profile (author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE) & (<p>Reporter: {{ object.author.first_name }} {{ object.author.last_name }}</p>)
