import os
import re

while True:
    directory = input("Путь к директории (или q для выхода): ")
    if directory.lower() in ["q", "quit"]:
        break

    # Цикл по всем файлам в директории на изменения регистра расширений
    for filename in os.listdir(directory):
        # Разделить имя файла на базовое имя и расширение
        basename, extension = os.path.splitext(filename)
        # Проверить, является ли расширение заглавным
        if extension.isupper():
            # Преобразовать расширение в строчные буквы
            new_extension = extension.lower()
            # Переименовать файл с новым расширением
            os.rename(os.path.join(directory, filename), os.path.join(directory, basename + new_extension))

    format_files = '.' + input('В каком формате файлы?: ')
    operation = input("Введите операцию (Зменить[1], Удалить[2] или Пропустить[3]): ")
    if operation == "1":
        target = input("Введите текст, который нужно заменить: ")
        replacement = input("Введите текст, на который нужно заменить: ")
    elif operation == "2":
        target = input("Введите текст, который нужно удалить: ")
        replacement = ""
    else:
        target = ""
        replacement = ""

    for file in os.listdir(directory):
        if file.endswith(format_files):
            # Заменить или удалить целевую часть имени файла
            new_name = re.sub(re.escape(target), replacement, file)
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_name)
            print(f"Переименование {old_path} в {new_path}")
            os.rename(old_path, new_path)

    print("Переименование завершено.")
