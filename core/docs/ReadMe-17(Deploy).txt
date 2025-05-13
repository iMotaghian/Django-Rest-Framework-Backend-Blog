# 17-1 [installation] NGINX (proxy connection) - GUNICORN
# NGINX: Optimize, deliver, and secure apps across the entire enterprise with NGINX (connect to GUNICORN)-> https://nginx.org/
# GUNICORN: Green Unicorn' is a Python WSGI HTTP Server for UNIX / server of our product in false debug -> https://gunicorn.org/

# 17-2 [] -> 2-بررسی پیش‌نیازهای پیاده‌سازی با استفاده از Docker.docx

# 17-3 [django GUNICORN] -> https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/gunicorn/
pip install gunicorn
# make docker-compose-stage.yml & docker-compose-prod.yml // stage phase and product phase
# docker-compose-stage.yml:
# add "gunicorn core.wsgi" to backend command /// This will start one process running one thread listening on 127.0.0.1:8000 -> https://docs.gunicorn.org/en/latest/
# Command line: -b ADDRESS or --bind ADDRESS /// Default: ['127.0.0.1:8000'] -> https://docs.gunicorn.org/en/latest/settings.html#bind
# backend > command: gunicorn core.wsgi --bind 0.0.0.0:8000 ///  set env DEBUG=False
docker-compose -f docker-compose-stage.yml up --build
# app became run but in this moment can't load statics
# make "staticfiles" folder in core // base on setting 
# edit backend command to : sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn core.wsgi:application --bind 0.0.0.0:8000"
docker-compose -f docker-compose-stage.yml up --build
# all file needed copied on static file, but still in web site can't loaded, now we need use "NGINX"

# 17-4 [NGINX] add "nginx" to servers of ocker-compose-stage.yml / image / container_name / ports / depends_on
docker-compose -f docker-compose-stage.yml up --build
# nginx ip: http://127.0.0.1:80/ /// after need connect NGINX to GUNICORN:
# need modify config of NGINX (ConfigNGINX.PNG): VScode > Docker > container > django-blog > nginx > files > etc > nginx > conf.d > default.conf
# edit "location /" -> https://gunicorn.org/#deployment ---> NGINX redirect ""http://127.0.0.1:8000/"" to GUNICORN "http://127.0.0.1:8000/" /// (this rule is not safe maybe file became delete)
# [okay rule] make "default.conf" in "Core" folder and go to docker-compose-stage.yml and add "volumes:" to "nginx:"
# also delet "ports:" in backend and set "expose:"
docker-compose -f docker-compose-stage.yml up
# "http://127.0.0.1:8000/" is not working / go to "http://127.0.0.1:8000/" /// all request transfer with NGINX to GUNICORN

# 17-5 [set static and media files] set "volumes: / static_volume: / media_volume:" for all services in end of docker compose
# first set address of static and media folder in "volumes" of "backend" > "static_volume:/app/static" & "media_volume:/app/media" (app is folder of docker that our proj added on)
# last set address of static and media folder in "volumes" of "nginx" > "static_volume:/home/app/static" & "media_volume:/home/app/media" (nginx need home/ dir first address)
# go to "default.conf" and set > "location /static/" & "location /media/"
docker-compose -f docker-compose-stage.yml up









