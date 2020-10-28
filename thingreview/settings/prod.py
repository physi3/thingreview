from .common import *

SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Let heroku handle settings.
from django_heroku import settings
settings(locals())
