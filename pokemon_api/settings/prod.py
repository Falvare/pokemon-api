from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['drf-pokemon.herokuapp.com']

CSRF_TRUSTED_ORIGINS = ['https://drf-pokemon.herokuapp.com/']