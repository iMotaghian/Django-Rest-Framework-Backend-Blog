# 14-1 [Stress test-Load test] Test site under presure
# locust: https://github.com/locustio/locust & https://locust.io/ & https://pypi.python.org/pypi/locust & https://docs.locust.io/en/stable/installation.html
# need run in docker -> https://docs.locust.io/en/stable/running-in-docker.html#docker-compose
# make a new branch in github and edit docker-compose.yml
# add to server:
master:
    image: locustio/locust
    ports:
     - "8089:8089"
    volumes:
      - ./:/mnt/locust
    command: -f /mnt/locust/locustfile.py --master -H http://backend:8000/
  
  worker:
    image: locustio/locust
    volumes:
      - ./:/mnt/locust
    command: -f /mnt/locust/locustfile.py --worker --master-host master

# add new folder and file address to -> core/locust/locustfile.py
# add address in docker-compose.yml in master & worker:
volumes:
      - ./core/locust:/mnt/locust

# make a class in locustfile.py "QuickstartUser"
# start docker-compose
docker-compose up -d
# -> 127.0.0.1:8089

#last docker compose: (docker-compose(load-test).txt)
master:
    image: locustio/locust
    ports:
     - "8089:8089"
    volumes:
      - ./core/locust:/mnt/locust
    command: -f /mnt/locust/locustfile.py --master -H http://backend:8000/
  
  worker:
    image: locustio/locust
    volumes:
      - ./core/locust:/mnt/locust
    command: -f /mnt/locust/locustfile.py --worker --master-host master


# 14-2 [locustfile.py] update class
# restart lucast
# -> 127.0.0.1:8089 - host :8000

# 14-3 [locustfile.py] update class / login users with jwt token and headers
# def on_start -> when code run - use for login
# 127.0.0.1:8089

# important : don't mix "Load-Test branch" with "main branch"


