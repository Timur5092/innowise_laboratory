# Используем официальный образ Python
FROM python:3.13

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY main.py .

# Устанавливаем зависимости
RUN pip install --no-cache-dir fastapi uvicorn

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Команда запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
