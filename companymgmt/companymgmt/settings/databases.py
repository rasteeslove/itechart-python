from companymgmt.settings.secrets import postgres_db_pass


LOCAL_DEV = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'companymgmtdb',
    'USER': 'krastsislau',
    'PASSWORD': postgres_db_pass,
    'HOST': '127.0.0.1',
    'PORT': '5432',
}

LOCAL_TEST = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'companymgmtdb_test',
    'USER': 'krastsislau',
    'PASSWORD': postgres_db_pass,
    'HOST': '127.0.0.1',
    'PORT': '5432',
}

DOCKER_DEV = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'postgres',
    'USER': 'container-lord',
    'PASSWORD': 'wh@tever',
    'HOST': 'dev_db',
    'PORT': '5432',
}

DOCKER_TEST = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': 'test_db',
    'PORT': '5432',
}
