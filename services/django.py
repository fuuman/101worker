import os
import sys

sys.path.append(os.path.dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'services.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

