# Question_Test_App

Разработать сайт для формирования и прохождения тестов(опросов).
На сайте должен присутствовать каталог/список всех тестов(опросов).
Для теста должна быть возможность указать входящие в него вопросы и порядковый номер вопроса в рамках этого теста(просто числом).
На странице каждого из тестов отображается описание теста и кнопка _"Пройти тест"_.
После нажатия на кнопку _"Пройти тест"_ пользователю отображается форма/список всех вопросов теста отсортированых по порядковому номеру и поля для ввода ответа на каждый вопрос.

Сущности:

```
- Test(тест)
- Question(вопрос)
- Testrun(прохождение теста)
```

В тесте может быть много вопросов,
один вопрос может быть в нескольких тестах.
Один тест можно пройти много раз.
При прохождении теста на каждый вопрос должен быть
сохранен ответ.

Так же, присутствуют логгеры и тесты.

To use this code you may copy repository:
```
git clone https://github.com/kyrylomytroshyn/Question_Test_App/
```

To launch this app, write the command bellow:

```
python manage.py runserver
```

Then, write 127.0.0.1:8000 in browser address line.

To lauch memcache server you need to install this app in your system.

All other requirements you can find in the requirements.txt.

To use celery (for background tasks) lauch celery-server:

Install redis and start redis-server.

IWrite the command bellow to check server status:
```
redis-cli ping
```
If you got "PONG" - congratulations!

1. Worker
```
celery -A worker -l info
```

2. Scheduler
```
celery -A picha beat -l info
```
