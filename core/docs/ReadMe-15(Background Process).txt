# 15-1 [Background Process] in Background Process we make a "Queue" (صف) and all task "FIFO" entered in to queue. "app" send task to "queue" and "queue" send tasks to empty "worker"
# if we don't have worker empty and Queue became full, jobs are lost! /// "Broker" (واسط) has move task from "App", "Queue", "worker" /// Broker (transport) module in django: redis , rabbitmq
# redis is Broker -> https://github.com/redis/redis
# python "Celery" can get communication between "Redis" (Broker) & Worker  -> https://docs.celeryq.dev/en/stable/getting-started/introduction.html


# 15-2 [Run redis in docker compose] port 6379:6379 is default for redis -> https://hub.docker.com/_/redis & https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/docker/
docker-compose exec backend sh
pip install redis
exit
docker-compose down
# make edit docker-compose.yml / add new services: (upper of backend)

redis:
    container_name: redis
    image: redis
    ports:
      - "6379:6379"
    command: redis-server --save 60 1 --loglevel warning

# save docker compose and run again
docker-compose up -d
# check redis: (cli -> command line)
docker-compose exec -it redis sh
redis-cli
ping
# return "PONG" -> it means redis is okay and our Broker is online now


# 15-3 [Run Celery] make new file in: "proj/proj/celery.py" (proj=core) // beside of settings.py -> https://docs.celeryq.dev/en/latest/django/first-steps-with-django.html
docker-compose exec backend sh
pip install celery
# update "proj/proj/__init__.py" -> from .celery import app as celery_app
# add to settings : CELERY_BROKER_URL -> set address of redis
# for run celery:
docker-compose exec backend sh
# celery -A proj worker -l INFO
celery -A core worker -l INFO
# return : Connected to redis://redis:6379/1


# 15-4 [add worker (celery) to docker compose] add depends_on: to backend in docker-compose.yml
docker-compose down
# add restart: always to redis in docker-compose
# add new services: to docker-compose ->  worker:
docker-compose up -d

# 15-5 [make task] make urls in "accounts/urls.py" -> path("send-email/", views.send_email, name="send-email"), and make "views" send_email()
# need delete "path("api/v1/", include("accounts.api.v1.urls"))," in urls.py
# make "tasks.py" in accounts folder and use "from celery import shared_task"
docker-compose down
docker-compose up
# go to http://127.0.0.1:8000/accounts/send-email/ , and after 3 sec in terminal print text / print('done sending email')


# 15-6 [Task Schedule & Beat] -> https://docs.celeryq.dev/en/latest/userguide/periodic-tasks.html#beat-custom-schedulers
# we can use Schedule in our project in 3 way

# [beat-1] add to setting CELERY_BEAT_SCHEDULE / name task - address of task function - time of period
# we must rest worker docker, also need active "beat":
docker-compose exec backend sh
celery -A core beat -l INFO
# export in terminal:
## [2025-04-27 21:39:57,866: INFO/MainProcess] Task accounts.tasks.sendEmail[475176f1-c554-4389-92c7-4f8dd25a65e9] received
## worker-1    | [2025-04-27 21:40:00,867: WARNING/ForkPoolWorker-8] done sending email
# for stop beat:
docker compose restart backend


# [beat-2] open "celery.py" and add decorative "@app.on_after_configure.connect" and function -> https://docs.celeryq.dev/en/latest/userguide/periodic-tasks.html#entries
# restart worker docker
docker-compose exec backend sh
celery -A core beat -l INFO


# [beat-3] use Custom scheduler classes -> https://docs.celeryq.dev/en/latest/userguide/periodic-tasks.html#using-custom-scheduler-classes
docker-compose exec backend sh
pip install django-celery-beat
exit
docker-compose exec worker sh
pip install django-celery-beat
# INSTALLED_APPS = ('django_celery_beat',)
docker-compose exec backend sh
python manage.py migrate
celery -A core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
# go to admin and enter "Periodic tasks" and select "add new Periodic tasks", make new task:
# each function that created on "tasks.py" loaded and we can select in "Task (registered):" field






