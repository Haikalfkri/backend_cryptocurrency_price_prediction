from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']