
database admining
-----------------
1. download or install from command line: https://www.postgresql.org/download/

2. log into psql
```
sudo -u postgres psql
```

3. create user with a password

create user my_user with password 'whateverYouWant';

4. give permission to user for altering db

ALTER ROLE my_user CREATEDB;

5. create the database

CREATE DATABASE record_store

6. change ownership of database (root should be in charge of it)

ALTER DATABASE record_store OWNER to my_user;

7. dump the sql file into the database:

psql my_user -h localhost -d record_store -f db.sql

* connect to database from localmachine

psql -d postgres -U my_user -h localhost

flask admining
--------------
1. install virtual environment in root folder 

python3 -m venv venv

2. activate virtual environment

. venv/bin/activate

3. install from requirements while in environment

pip install -r requirements.txt

4. create a .env file in the root folder for the database string. the variable namse are in db.py

vim .env

5. paste the following:
```
HOST=localhost
DATABASE=record_store
USER=my_user
PASSWORD=whateverYouWant
```
5. run app (in debug mode)

flask --app app --debug run

