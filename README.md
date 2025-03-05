# Project Title

Order Processing System.

## Description

This project is about handling large number of order request using Python, FastApi, PostgresSQL.

## Getting Started


### Installing

* Python version - 3.8+
* FastApi[Standard]
* PostgresSQL
* Redgate Flyway

### Configration

* ecommerce/flyway/flyway.conf - 
    * flyway.url=<DB_URL>
    * flyway.user=<DB_USER_NAME>
    * flyway.password=<DB_PASSWORD>

* ecommerce/backend/config.properties -
    * DB_HOST = <DB_HOST>
    * DB_USER_NAME = <DB_USER_NAME>
    * DB_PASSWORD = <DB_PASSWORD>
    * DB_PORT = <DB_PORT>
    * DB_NAME = <DB_NAME>

### Executing program

* How to run the program
* Step-by-step bullets

* Go to flyway folder
```
flyway migrate
```

* Go to backend folder
```
fastapi dev main.py
```

## Authors

Contributors names and contact info

Himanshu Patel 
ex. [@himan0610](https://github.com/himan0610)