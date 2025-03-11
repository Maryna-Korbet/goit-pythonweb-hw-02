# Використовуємо легку версію Python 3.10
FROM python:3.10-slim

# Встановимо змінну середовища
ENV APP_DIR /app

# Встановимо робочу директорію
WORKDIR ${APP_DIR}

# Скопіюємо файли в контейнер
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо всі файли (окрім `requirements.txt`, який ми вже скопіювали)
COPY . .

# Відкриваємо порт
EXPOSE 8000

# Запускаємо FastAPI через Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]