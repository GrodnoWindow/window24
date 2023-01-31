command = '/home/dev/windows24-backend/env/bin/gunicorn'
pythonpath = '/home/dev/windows24-backend/backend/'
bind = '127.0.0.1:8001'
workers = 3
user = 'dev'
limit_request_fields = 32000
limit_request_fields_size = 0
rav_env = 'DJANGO_SETTINGS_MODULE=config.settings'
