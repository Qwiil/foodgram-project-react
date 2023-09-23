Foodgram - продуктовый помощник с базой кулинарных рецептов. Позволяет публиковать рецепты, сохранять избранные, а также формировать список покупок для выбранных рецептов. Можно подписываться на любимых авторов.

### Технологии:

Python, Django, Docker, Gunicorn, NGINX, PostgreSQL.

Проект доступен [http://84.201.162.72/]

### Развернуть проект на удаленном сервере:

- Клонировать репозиторий:
```
git@github.com:Qwiil/foodgram-project-react.git
```

- Установить на сервере Docker, Docker Compose:

```
sudo apt install curl                                   # установка утилиты для скачивания файлов
curl -fsSL https://get.docker.com -o get-docker.sh      # скачать скрипт для установки
sh get-docker.sh                                        # запуск скрипта
sudo apt-get install docker-compose-plugin              # последняя версия docker compose