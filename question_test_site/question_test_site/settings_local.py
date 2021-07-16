
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.python setup.py build",
        "NAME": 'tests',
        "USER": 'test_admin',
        "PASSWORD": 'pass',
        "HOST": "127.0.0.1",
        "PORT": "5432"
    }
}


