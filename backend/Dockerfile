FROM python:3.12

WORKDIR /app

# Установка Gunicorn
RUN pip install gunicorn==23.0.0

# Копирование requirements.txt и установка зависимостей
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# Копирование всего проекта
COPY . .

# Команда запуска Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kittygram_backend.wsgi"]
