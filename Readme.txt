Создайте новый образ и запустите два контейнера:
https://django.fun/tutorials/dokerizaciya-django-s-pomoshyu-postgres-gunicorn-i-nginx/
$ docker-compose up -d --build
Запустить контейнер
$ docker-compose up
Запустите миграции:
$ docker-compose exec web python manage.py migrate --noinput
Войти в командную строку контейнера
$ docker-compose exec [имя контейнера] sh или bash
$ docker-compose exec crm_api sh