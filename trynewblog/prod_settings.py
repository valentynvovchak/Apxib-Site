import os
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY')


DEBUG = False

ALLOWED_HOSTS = ['apxib.site', 'apxib', 'www.apxib.site', 'www.apxib', '127.0.0.1', 'apxib-site.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/media/')

ADMINS = (('Valentyn', 'valentyn.vovchak@gmail.com'),)
MANAGERS = (('Valiunya', 'valiunyavovchak@gmail.com'),)


# S3 BUCKETS CONFIG

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# [
#     {
#         "AllowedHeaders": [
#             "*"
#         ],
#         "AllowedMethods": [
#             "GET",
#             "PUT",
#             "POST",
#             "HEAD",
#             "DELETE"
#         ],
#         "AllowedOrigins": [
#             "*"
#         ],
#         "ExposeHeaders": [],
#         "MaxAgeSeconds": 3000
#     }
# ]

