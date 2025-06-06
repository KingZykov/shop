# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/n/ninazyq7/ninazyq7.beget.tech/cloud_play')
sys.path.insert(1, '/home/n/ninazyq7/ninazyq7.beget.tech/venv/lib/python3.13/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cloud_play.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
