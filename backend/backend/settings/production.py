from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY=os.environ.get('PROD_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']