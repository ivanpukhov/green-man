import os
from bs4 import BeautifulSoup

# Путь к вашей директории
directory = '/Users/ix/WebstormProjects/green-man/client_annotation'

# Пройти по всем файлам в директории
for filename in os.listdir(directory):
    if filename.endswith('.html'):  # проверить, является ли файл HTML-файлом
        filepath = os.path.join(directory, filename)  # получить полный путь к файлу

        # Открыть файл для чтения и записи
        with open(filepath, 'r+') as f:
            soup = BeautifulSoup(f, 'html.parser')

            # Найти и удалить все теги script
            for script in soup("script"):
                script.decompose()

            # Перейти в начало файла и перезаписать его с измененным содержимым
            f.seek(0)
            f.write(str(soup))
            f.truncate()  # удалять содержимое файла после текущей позиции
