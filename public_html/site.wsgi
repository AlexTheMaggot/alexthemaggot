import os, sys
activate_this = '/home/a0451711/python/bin/activate_this.py'
with open(activate_this) as f:
  exec(f.read(), {'__file__': activate_this})
sys.path.insert(0, os.path.join('/home/a0451711/domains/alexthemaggot.ru/alexthemaggot'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'alexthemaggot.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()