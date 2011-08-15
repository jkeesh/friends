import os
import sys

sys.path.append('/home/jkeesh/sites/friends')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

print >> sys.stderr, "debuggginggggg"

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()