# QACloudCamp

инструкция по поднятию проекта:

Создайте новый проект в выбранной вами IDE (например, PyCharm).
Установите необходимые библиотеки в терминале requests и pytest через pip: pip install requests, pip install pytest
Создайте папку tests в корневой директории проекта.
В папке tests создайте test_api.py файл.
Напишите тесты
Запустите терминал в папке с файлом test_api.py
Запустите тесты, введя в терминале следующую команду: python pytest. 


команда запуска Dockerfile:

"docker build -t api_tests . && docker run -it --rm api_tests"- собирает образ и запускает контейнер Docker

