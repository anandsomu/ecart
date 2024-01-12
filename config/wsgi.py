"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
