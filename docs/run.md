## Project Launch

### Prerequisites
Before running the project, make sure you have **Docker** and **Docker compose** installed on your system.

### Install the project
``
docker compose up --build
``

go to backend container and attach shell:
```
flask db init
flask db migrate
flask db upgrade
```

Now you should have backend running on **localhost:4000**,frontend on **localhost:5173** and database on **localhost:5432**
