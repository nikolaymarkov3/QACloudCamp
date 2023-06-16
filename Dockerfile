# используем официальный образ Python версии 3.9
FROM python:3.10

# устанавливаем зависимости
RUN pip install requests pytest

# копируем файлы проекта в образ
COPY . /app

# переключаем рабочую директорию на /app
WORKDIR /app

# указываем команду для запуска тестов
CMD ["pytest", "-v"]