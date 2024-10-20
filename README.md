
# CismTestWork

Необходимо разработать веб-сервис блога с базовым функционалом, используя Python и один из предложенных фреймворков.
____

## Инструкция по установке и запуску

Клонируем проект

```bash
  git clone https://github.com/CodeFramer0/cism-test-work.git
```

Идем в рабочую директорию

```bash
  cd cism-test-work
```

Настраиваем окружение

```bash
  cp .env.template .env
```
Обновите .env файл, если необходимо.

Собираем и запускаем контейнеры
Для сборки проекта и его запуска в контейнерах выполните следующую команду:
```bash
  docker compose -f "docker-compose.yml" up -d --build 
```


После успешного запуска проект будет доступен по следующим URL:

Админ панель: http://localhost/admin/ <br>
Swagger документация API: http://localhost/api/swagger/<br>
Redoc документация API: http://localhost/admin/redoc/<br>
____
# Создание суперпользователя
Для управления данными через админ панель необходимо создать суперпользователя. Следуйте этим шагам:
 Присоединяемся к терминалу запущенного контейнера

```bash
  docker exec -it cism_django bash
```
 Создаем суперпользователя

```bash
  python manage.py createsuperuser --username=joe --email=joe@example.com
```
Задайте пароль и подтвердите его.

____
## Запуск тестов

Чтобы запустить тесты, выполните следующие команды:

```bash
    docker exec -it cism_django bash
    python manage.py test
```
 

