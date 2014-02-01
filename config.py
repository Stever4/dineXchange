import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'J\xa6\xd4B\x1c\xa5!\xa5f\xe5\x9d~@\xd66\xb5\xf8\xae\x9fp\xe7\x1c\x17['

OPENID_PROVIDERS = [ {'name': 'Google', 'url': 'https://www.google.com/acounts/o8/id'}]
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
