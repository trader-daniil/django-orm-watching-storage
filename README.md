# Данный код возвращает информацию о пропусках и визитах сотрудников

### Описание

Программа получает доступ к базе данных и возвращает информацию о сотрудниках, пропусках и активных посещениях. Если пользователь провел в хранилище более одного часа, то его визит можно назвать подозрительным

#### Доступные url

[http://127.0.0.1:8000/](http://127.0.0.1:8000/) - главная страница сайта, содержащая список всех сотрудников. Нажатием на имя сотрудника приводит к подробной информации о его посещениях

[http://127.0.0.1:8000/passcard_info/<номер_пропуска>](http://127.0.0.1:8000/passcard_info/7ef4341f-ff94-4a32-a009-0aa43cf98bf0) - покажет нам подробную информацию о посещениях данного сотрудника(с конкретным пропуском)

[http://127.0.0.1:8000/storage_information](http://127.0.0.1:8000/storage_information) - информация о сотрудниках, находящихся в данный момент в хранилище

### Установка

Python должен быть установлен. Затем используйте pip (или pip3 если есть конфликт с Python2) для установки зависимостей. Затем создайте виртуальное окружение и в терминале выполните команду по установке зависимостей:

```
pip install -r requirements.txt
```

Настройте переменные окружения для работы с Базой Данных:

* DB_ENGINE
* DB_HOST
* DB_PORT
* DB_NAME
* DB_USER
* DB_PASSWORD

### Запуск

Для запуска программы введите в терминале команду:

```
python manage.py
```