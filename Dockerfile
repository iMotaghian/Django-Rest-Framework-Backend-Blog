# install operiontion app (python , php , ...)
FROM python:3.11-slim


# set env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set default directory
WORKDIR /app

# copy requirements to app folder < . > is default folder
COPY requirements.txt /app/

# update pip to last verison
RUN python -m pip install --upgrade pip

# install package > requirements.txt
RUN pip install -r requirements.txt

# copy all dir to app
COPY ./core /app/

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# docker build -t django .
# docker run -p 8000:8000 django