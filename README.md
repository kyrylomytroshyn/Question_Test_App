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


To run this app with docker-compose write the commands bellow:

```
 docker-compose build
 docker-compose up -d --remove-orphans
 docker-compose exec backend python3 manage.py migrate

```

