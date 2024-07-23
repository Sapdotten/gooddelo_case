# FastAPI app
Этот проект представляет собой resful api, разработанный согласно заданию из файла  `task.md`.

## Требования
* Python 3.9 (для запуска без Docker)
* Docker (для запуска через Docker)

## Содержимое проекта
* `Dockerfile` - файл конфигурации Docker
* `requirements.txt` - файл с зависимостями Python
* `app/` - директория с кодом проекта
* `README.MD` - этот файл с инструкцией
* `app/configs.json` - файл с настройками генерации JWT-токенов

## Настройка переменных окружения перед запуском

Необходимо создать файл .env в корневой директории проекта, где нужно указать следующие **переменные окружения**:

* `JWT_SECRET` - ключ для генерации JWT-токенов
* `SQL_USER` - имя пользователя PostgreSQL
* `SQL_PASSWORD` - пароль для пользователя PostgreSQL
* `SQL_HOSTNAME` - хост базы данных (с указанием порта) PostgreSQL
* `SQL_DATABASE_NAME` - имя базы данных PostgreSQL
* `REDIS_HOST` - хост базы данных Redis

Дополнительно, но не обязательно можно указать:
* `REDIS_USER` - имя пользователя базы данных Redis
* `REDIS_PASSWORD` - пароль пользователя базы данных Redis
* `REDIS_DB` - номер базы данных Redis

## Инструкция по запуску с использованием Docker
### 1. Клонируйте репозиторий

```bash
git clone https://github.com/Sapdotten/gooddelo_case.git
cd <..>/gooddelo_case
```

### 2. Убедитесь в том, что есть файл env.txt

### 3. Соберите Docker-образ
```bash
docker build -t my-app .
```

### 4. Запустите контейнер
```bash
docker run -p 5000:5000 my-app
```

### 5. Пользуйтесь

API работает по адресу http://localhost:5000

**Документация**: http://localhost:5000/docs

## Инструкция по запуску **без** использования Docker
### 1. Клонируйте репозиторий

```bash
git clone https://github.com/Sapdotten/gooddelo_case.git
cd <..>/gooddelo_case
```

### 2. Создайте виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate  
# Для Windows используйте `venv\Scripts\activate\bat`
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Убедитесь в том, что есть файл .env

### 5. Запустите приложение
```bash
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```


### 6. Пользуйтесь

API работает по адресу http://localhost:5000

**Документация**: http://localhost:5000/docs
