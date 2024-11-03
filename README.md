# Django Wedding Manager
- Using Django

## Features
First application using Django, this app is an online wedding gift list, where there are two sides: one for the bride/groom and another for the guests.
Its functionalities are simple.
### Bride/Groom
- Add guests and their companion limits
- Add gifts, with their photo, price, and importance level

### Guest
- Reserve the gifts that the bride and groom want
- Define their companions

## How to use
- (Optional) create a Python virtual environment

- activate it
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

- install Django
    ```bash
    pip install django
    ```

- Run makemigrations from manage.py to update the migrations
    ```bash
    python manage.py makemigrations
    ```

- Run migrate from manage.py to apply the migrations to the database
    ```bash
    python manage.py migrate
    ```

- Run runserver to start the API
    ```bash
    python manage.py runserver
    ```