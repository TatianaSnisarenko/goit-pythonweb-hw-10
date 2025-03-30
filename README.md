# Contacts API

Contacts API is a RESTful API for managing contacts for each user separately using an authentication mechanism. It provides functionality to create, read, update, and delete contacts, as well as search for contacts and retrieve a list of contacts with upcoming birthdays. Additionally, users can view their profile information and update their avatar. The application includes an email verification feature that sends a confirmation email to users upon registration. This ensures that only valid email addresses are used for account creation.

## Features

### Core Functionality:

1. **CRUD Operations**:

   - User Registration with email verifiation
   - User Login
   - Create a new contact.
   - Retrieve a list of contacts with pagination.
   - Retrieve a single contact by its ID.
   - Update an existing contact by its ID.
   - Delete a contact by its ID.
   - View personal profile information.
   - Update profile avatar.

2. **Search Contacts**:

   - Search by first name, last name, or email with pagination.

3. **Upcoming Birthdays**:
   - Retrieve a list of contacts with birthdays in the next `n` days (default: 7 days) with pagination.

## Prerequisites

- Python 3.8+
- Docker

## Setup and Usage

### Step 1: Start a PostgreSQL Container

Run the following command (replace all values in `{}`) to start a PostgreSQL container:

```sh
docker run --name {container_name} -p {postgres_port}:5432 -e POSTGRES_USER={postgres_user} -e POSTGRES_PASSWORD={postgres_password} -d postgres
```

Create a database with the name `contact_db`:

```sh
docker exec -it {container_name} psql -U {postgres_user}
CREATE DATABASE {db_name};
exit;
```

### Step 2: Create a `.env` file and set the following values:

```env
POSTGRES_DB={db_name}
POSTGRES_USER={postgres_user}
POSTGRES_PASSWORD={postgres_password}
POSTGRES_PORT={postgres_port}
POSTGRES_HOST={postgres_host}

DB_URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
JWT_SECRET=your_secret_key
JWT_ALGORITHM=HS256
JWT_EXPIRATION_SECONDS=3600

MAIL_USERNAME={email_address}
MAIL_PASSWORD={email_password}
MAIL_FROM={email_address}
MAIL_PORT={port}
MAIL_SERVER={smrp_server}
MAIL_FROM_NAME=Contacts API Service
MAIL_STARTTLS=False
MAIL_SSL_TLS=True
USE_CREDENTIALS=True
VALIDATE_CERTS=True
```

Ensure that the email account you use has SMTP enabled.

### Step 3: Install Dependencies

Ensure you have a virtual environment activated, then install dependencies:

```sh
pip install -r requirements.txt
```

### Step 4: Configure and Apply Migrations

Use Alembic to manage database migrations. To create and apply the initial migration, run:

```sh
alembic init migrations
```

#### Configure `env.py`

Replace the beginning of the `migrations/env.py` file with the following code:

```python
import asyncio
from logging.config import fileConfig

from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool

from alembic import context

from database.models import Base
from conf.config import config as app_config
```

Find the following line in `env.py`:

```python
target_metadata = None
```

Replace `None` with:

```python
target_metadata = Base.metadata
```

Replace the database connection string with the actual connection:

```python
config.set_main_option("sqlalchemy.url", app_config.DB_URL)
```

Modify the `run_migrations_online` function for asynchronous migrations:

```python
def run_migrations(connection: Connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations():
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(run_migrations)

    await connectable.dispose()

def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())
```

Apply the migrations:

```sh
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### Step 5: Run the Application

Start the FastAPI server:

```sh
fastapi dev src/main.py
```

### Use Swagger for API Exploration

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

# Contacts API

Contacts API is a RESTful API for managing contacts для кожного юзера окремо за допомогою механізму автентифікації. It provides functionality to create, read, update, and delete contacts, as well as search for contacts and retrieve a list of contacts with upcoming birthdays. Також можна переглядати інформацю щодо себе і оновлювати свій аватар

## Features

### Core Functionality:

1. **CRUD Operations**:

- Регістрація
- Логін
- Create a new contact.
- Retrieve a list of contacts with pagination.
- Retrieve a single contact by its ID.
- Update an existing contact by its ID.
- Delete a contact by its ID.
- Перегляд інформацї щодо себе
- Оновлення свого аватару

2. **Search Contacts**:

   - Search by first name, last name, or email with pagination.

3. **Upcoming Birthdays**:
   - Retrieve a list of contacts with birthdays in the next `n` days (default: 7 days) with pagination.

## Prerequisites

- Python 3.8+
- Docker

## Setup and Usage

### Step 1: Start a PostgreSQL Container

Run the following command(replace all values in {})to start a PostgreSQL container:

```sh
docker run --name {container_name} -p {porstres_port}:5432 -e POSTGRES_USER={postres_user} -e POSTGRES_PASSWORD={postrges_password} -d postgres
```

Create database with name: contact_db

```sh
docker exec -it hw10-db psql -U hw10
CREATE DATABASE {db_name};
exit;
```

### Step 2: Create file with name .env and put or edit the following values:

POSTGRES_DB=db_name
POSTGRES_USER=postres_user
POSTGRES_PASSWORD=postrges_password
POSTGRES_PORT=porstres_port
POSTGRES_HOST=postgres_host

DB_URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
JWT_SECRET=your_secret_key
JWT_ALGORITHM=HS256
JWT_EXPIRATION_SECONDS=3600

### Step 3: Install Dependencies

Ensure you have a virtual environment activated, then install dependencies:

```sh
pip install -r requirements.txt
```

### Step 3: Configure and Apply Migrations

Use Alembic to manage database migrations. To create and apply the initial migration, run:

'''sh
alembic init migrations
'''

configure env.py

Замініть початок файлу migrations/env.py на наступний код:

import asyncio
from logging.config import fileConfig

from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool

from alembic import context

from database.models import Base
from conf.config import config as app_config

Далі нам необхідно знайти наступний рядок нижче в коді файлу env.py:

target_metadata = None

і замість None вказати наші метадані:

target_metadata = Base.metadata

Тут виконаємо заміну рядка підключення до бази даних на актуальну:

config.set_main_option("sqlalchemy.url", app_config.DB_URL)

Ми хочемо виконувати міграції асинхронно, бо в нашому вебзастосунку ми використовуємо асинхронний підхід при роботі з базою даних. Перепишемо повністю функцію run_migrations_online у файлі env.py.

def run_migrations(connection: Connection):
context.configure(connection=connection, target_metadata=target_metadata)
with context.begin_transaction():
context.run_migrations()

async def run_async_migrations():
connectable = async_engine_from_config(
config.get_section(config.config_ini_section, {}),
prefix="sqlalchemy.",
poolclass=pool.NullPool,
)

    async with connectable.connect() as connection:
        await connection.run_sync(run_migrations)

    await connectable.dispose()

def run_migrations_online() -> None:
"""Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    asyncio.run(run_async_migrations())

```sh
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### Step 4: Run application using command

Start the FastAPI server:

```sh
fastapi dev src/main.py
```

Перший крок — зареєструвати нового користувача в нашій системі. Відправимо POST-запит на endpoint реєстрації http://127.0.0.1:8000/api/auth/register з наступними даними:

{
"username": "usertest",
"email": "test@api.com",
"password": "123456"
}

Використовуйте Postman для відправлення запиту.

Після реєстрації наступний крок — автентифікація користувача для отримання токенів доступу. Виберіть режим x-www-form-urlencoded для імітації відправлення форми. Відправте POST-запит на endpoint автентифікації http://127.0.0.1:8000/api/auth/login з наступними полями:

username: використовуйте username користувача usertest.
password: пароль користувача (123456).

Використовуйте Postman для відправлення запиту.

Очікувана відповідь міститиме токен доступу.

Цей токен буде необхідний для авторизації подальших запитів.

Тепер, коли ми автентифіковані, створимо новий тег. Підготуйте POST-запит до відповідного endpoint /api/tags. У заголовку запиту додамо отриманий access_token. Відкрийте вкладку 'Headers' для запиту та додайте новий заголовок з наступними параметрами:

Key: Authorization
Value: Bearer access_token

### Use swagger to perform available commands

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
