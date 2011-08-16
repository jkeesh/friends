## Visualize Your Facebook Friends


## Setup

### Prereqs

    You have django installed https://www.djangoproject.com/
	You have south installed http://south.aeracode.org/
	You have the fb python sdk https://github.com/facebook/python-sdk
	You have django-extensions http://packages.python.org/django-extensions/

### Create Database

Default is mysql. If you want to use sqlite, just change the django backends settings.

    $ mysql
    mysql> create database friends character set utf8;


### Sync Database

    ./manage.py syndb

Don't create a superuser account.

    ./manage.py migrate

### Setup secrets

Make a new facebook app and set the url to be localhost:8000. Create a python file called secrets.py in the top level directory. In here create a dictionary called local containing your facebook app id and facebook secret key.

	## secrets.py
    LOCAL = {}
    LOCAL['FACEBOOK_APP_ID'] =   "#####" 
    LOCAL['FACEBOOK_APP_SECRET'] =   "XXXXXX"

This way you can use your own facebook app.


### Runserver

    ./manage.py runserver


### Setup Cronjob

Set up a daily cronjob to update the list. Insert your project directory where I have 
cd /Users/jkeesh/Dropbox/Documents/CS/projects/friends

Edit your users crontab.

    crontab -e

Set the path and code to run.

    PATH=<make sure your path includes your python and django installations>
    01 7   *  *    *    cd <your project directory> && python manage.py create_data_point


For me:

    PATH=/sw/bin:/sw/sbin:/opt/local/bin:/opt/local/sbin:/Library/Frameworks/Python.framework/Versions/Current/bin:/opt/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/git/bin:/usr/texbin:/usr/X11/bin:/usr/local/sbin:/usr/local/mysql/bin:/Users/jkeesh/bin:/usr/X11R6/bin
    01 7   *  *    *    cd /Users/jkeesh/Dropbox/Documents/CS/projects/friends && python manage.py create_data_point


### Login!


Email me jkeesh@gmail.com with questions
