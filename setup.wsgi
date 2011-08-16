import os
import sys

sys.path.append('/home/jkeesh/sites/friends')
print >> sys.stderr, sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'friends.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()