from companymgmt.settings.secrets import postgres_db_pass, docker_postgres_db_pass


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
    'NAME': 'docker_companymgmtdb',
    'USER': 'container-lord',
    'PASSWORD': docker_postgres_db_pass,
    'HOST': 'cmgmt_db',
    'PORT': '5432',
}

DOCKER_TEST = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': 'cmgmt_db',
    'PORT': '5432',
}
