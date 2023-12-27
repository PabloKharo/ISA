# Сначала укажем базовый образ Python
FROM python:3.11

WORKDIR /backend

# Копируем папку common внутрь образа
COPY ./common /backend/common

# Устанавливаем зависимости
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем код сервера 1 внутрь образа
COPY ./service_topics /backend/server

# Указываем рабочую директорию
WORKDIR /backend/server

# Запуск сервера 1
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
