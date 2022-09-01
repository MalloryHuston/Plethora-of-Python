# Build a Microblog with Flask

This is an example web application using Python and the Flask framework.

## Instructions

Create a virtual environment in Python:

```
python -m venv venv (Windows)
python3 -m venv venv (Mac OS and Linux)
```

Start your virtual environment in Python by running:

```
venv\Scripts\activate (Windows)
source venv/bin/activate (Mac OS and Linux)
```

Username information and passwords:
```
user1: robert@example.com
password: monster
user2: david@example.com
password: seattle
```

To create the migration repository and all the database migrations, enter the following commands:
```
flask db init
flask db migrate -m "users table"
flask db upgrade
flask db migrate -m "posts table"
flask db upgrade
flask db migrate -m "new fields in user model"
flask db upgrade
```

To enter information into the Flask database, run the following command:
```
flask shell
```

Once you are ready to run your app, please enter this final command:
```
flask run
```

Then open up your web browser and enter the following URL in the address field:
```
http://localhost:8000/
```

## Requirements
```
pip install flask
pip install python-dotenv
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-login
pip install email-validator
```

## Citations
Grinberg, Miguel. (August 2022) The Flask Mega-Tutorial (last updated May 2018)[Source Code]. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world