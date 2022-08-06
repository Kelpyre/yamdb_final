# api_yamdb
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Живопись» или «Ювелирка»).

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

### requirements

Файл со списком необходимых модулей можно найти в /api_yamdb/requirements.txt

### Основные ресурсы api:

- AUTH - Регистрация пользователей и выдача токенов
- CATEGORIES - Категории (типы) произведений
- GENRES - Категории жанров
- TITLES - Произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- REVIEWS - Отзывы
- COMMENTS - Комментарии к отзывам
- USERS - Пользователи

### Примеры запросов:

#### Регистрация нового пользователя:
POST /v1/auth/signup/ HTTP/1.1
Content-Type: application/json
{
  "email": "foo@mail.com",
  "username": "foo"
}

#### Получение JWT-токена
POST /api/v1/auth/token/ HTTP/1.1
Content-Type: application/json
{
  "username": "foo",
  "confirmation_code": "bar"
}

#### Добавление произведения
POST /api/v1/titles/ HTTP/1.1
Content-Type: application/json
{
  "name": "foo",
  "year": 0,
  "description": "foobar",
  "genre": [
    "bar",
  ],
  "category": "barfoo"
}

#### Изменение данных пользователя
PATCH /api/v1/users/{username}/ HTTP/1.1
Content-Type: application/json
{
  "first_name": "foo",
  "last_name": "bar",
  "bio": "foobar"
}

#### Удаление жанра
DELETE /api/v1/genres/{slug}/ HTTP/1.1

```
Более подробнее см в /redoc/
```

### Шаблон наполнения .env файла:

Файл .env описывает переменные окружения, текущей конфигурацией предполагается его расположение в /infra. Пример его заполнения:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=Qwerty123 # пароль для подключения к БД(задать собственный)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
SECRET_KEY=* # секретный ключ
```

### Как запустить проект в Docker:

Перейти в директорию /infra/

Выполнить docker-compose up

По завершении сборки выполнить следующий набор команд:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```
Админская панель доступна по адресу http://localhost/admin

### Наполнение базы данными:

Команда для выгрузки дампа базы данных:
```
docker-compose exec web python manage.py dumpdata > dump.json 
```
Команда для загрузки данных в базу:
```
docker-compose exec web python manage.py loaddata dump.json
```

### Примеры запросов:

К проекту подключен модуль redoc, содержащий документацию по доступным эндпоинтам и примерам запросов. Адрес для redoc - [base]/redoc/.

### Применение команды csv_to_sql:

В проекте реализована собственная команда csv_to_sql для автоматического заполнения моделей в БД из .csv файлов. Синтаксис команды - python manage.py csv_to_sql <путь_до_csv> <название_модели>.

### Авторы проекта:

- Команда Яндекс.Практикума
- Дмитрий Филимонов - Тимлид
- Григорьева Мария - Разработчик
- Максимов Владислав - Разработчик
