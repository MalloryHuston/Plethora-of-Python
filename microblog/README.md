# Build a Microblog with Flask

This is an example web application using Python and the Flask framework.

## Instructions

Create a virtual environment in Python:

```
python -m venv venv
```

Start your virtual environment in Python by running:

```
venv\Scripts\activate (Windows)
source venv/bin/activate (Mac OS and Linux)
```

Username information and passwords:
```
1 david david@example.com seattle
2 robert robert@example.com monster
3 brittany brittany@example.com marketing
4 trista trista@example.com nursing
```

To create the migration repository and all the database migrations, enter the following commands:
```
(venv) $ flask db init
(venv) $ flask db migrate -m "users table"
(venv) $ flask db migrate -m "posts table"
(venv) $ flask db migrate -m "new fields in user model"
(venv) $ flask db migrate -m "followers"
(venv) $ flask db upgrade
```

To enter information into the Flask database, run the following command:
```
(venv) $ flask shell
```

Once you are ready to run your app, please enter this final command:
```
(venv) $ flask run
```

Then open up your web browser and enter the following URL in the address field:
```
http://localhost:9000/
```

## Troubleshooting

To receive error handling from the site via email, please open a second terminal session and enter the following;
```
(venv) $ python -m smtpd -n -c DebuggingServer localhost:8025
```

Leave this session running and go back to the first terminal to enter the following before running the application:
```
(venv) $ export MAIL_SERVER=localhost
(venv) $ export MAIL_PORT=8025
```
<b>On Windows, please use ```set``` instead of ```export```.</b>

Or if you want emails sent for real, you can use a real email server by entering the following below in your terminal:
```
(venv) $ export MAIL_SERVER=smtp.googlemail.com
(venv) $ export MAIL_PORT=587
(venv) $ export MAIL_USE_TLS=1
(venv) $ export MAIL_USERNAME=<your-gmail-username>
(venv) $ export MAIL_PASSWORD=<your-gmail-password>
```

## Requirements
```
pip install flask
pip install python-dotenv
pip install flask-wtf
pip install email-validator
pip install flask-mail
pip install pyjwt
```

## Citations
Grinberg, Miguel. (August 2022) The Flask Mega-Tutorial (last updated May 2018)[Source Code]. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
