# Flask-demo

공부용 프로젝트

공부 해야할 순위
1. Flask Routing
2. Flask Response
3. Flask User Login
4. Flask Folder Struct
5. Flask User Login with Redis
6. SqlAlchemy connect to postgres
7. Run on Docker-Compose


## 1. Docker
````dockerfile
FROM python:3.6

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .  ./

EXPOSE 8080

CMD [ "python3", "/app/bin/run.py" ]
````

## 2. Docker Compose
```dockerfile
# docker-compose.yml
version: '3'
services:
    postgres:
        image: postgres:10
        environment:
            - POSTGRES_DB=developer
            - POSTGRES_USER=developer
            - POSTGRES_PASSWORD=devpassword
        volumes:
            - postgres-data:/var/lib/postgresql/data
        ports:
            - "127.0.0.1:25000:5432"
    redis:
        image: redis:latest
        ports:
            - "127.0.0.1:25100:6379"
        command: redis-server --save ""
    backend:
      build: .
      tty: true
      volumes:
        - .:/app
      ports:
        - "8080:8080"


volumes:
    postgres-data:
        driver: local
```