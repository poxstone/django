# Python django
- [doc]()
- 
## run/install
￻- Prepare
```bash
python3 -m virtualEnv;
source virtualEnv/bin/activate;

pip install -r requirements.txt --upgrade;

cd djproject;
python manage.py runserver 0.0.0.0:8080;
```

## run interactive
```bash
# interactive
python manage.py shell;

# create app in project
python manage.py startapp users;

# admin superuser
python manage.py createsuperuser;
```

## Database
- ** Preload DB models (py history) **:
    `python djproject/manage.py makemigrations`
- ** Write DB models **:
    `python djproject/manage.py migrate`
- ** Run docker SQLite3 client**
    ```bash
    docker run --rm -it --name sqlite -v ${PWD}:/root/db/ nouchka/sqlite3;
    ```
- ** Project **
    ```bash
    sqlite> attach "djproject/db.sqlite3" as bd1;
    sqlite> .databases
    sqlite> .tables
    sqlite> .schema db1.posts_users
    sqlite> SELECT * FROM db1.posts_users;
    ```
