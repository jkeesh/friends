## Visualize Your Facebook Friends


## Setup

### Create Database

    $ mysql
    mysql> create databse friends character set utf8;


### Sync Database

    ./manage.py syndb

Don't create a superuser account.

    ./manage.py migrate


### Runserver

    ./manage.py runserver


### Setup Cronjob

Set up a daily cronjob to update the list. Insert your project directory where I have 
cd /Users/jkeesh/Dropbox/Documents/CS/projects/friends

    crontab -e

    			       	
	
    PATH=<make sure your path includes your python and django installations>
    01 7   *  *    *    cd <your project directory> && python /Users/jkeesh/Dropbox/Documents/CS/projects/friends/manage.py create_data_point


For me:

    PATH=/sw/bin:/sw/sbin:/opt/local/bin:/opt/local/sbin:/Library/Frameworks/Python.framework/Versions/Current/bin:/opt/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/git/bin:/usr/texbin:/usr/X11/bin:/usr/local/sbin:/usr/local/mysql/bin:/Users/jkeesh/bin:/usr/X11R6/bin
    01 7   *  *    *    cd /Users/jkeesh/Dropbox/Documents/CS/projects/friends && python /Users/jkeesh/Dropbox/Documents/CS/projects/friends/manage.py create_data_point


### Login!
