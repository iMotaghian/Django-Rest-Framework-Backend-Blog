# 12-1 [Faker] -> https://pypi.org/project/Faker/
docker-compose exec backend sh
pip install Faker
# from faker import Faker / fake = Faker() / fake.name()

# 12-2 [custom django-admin commands] -> https://docs.djangoproject.com/en/5.2/howto/custom-management-commands/
# make file To implement the command, edit core/blog/management/commands/insert_data.py 
docker-compose exec backend sh
python manage.py insert_data