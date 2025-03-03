from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY=os.environ.get('PROD_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}