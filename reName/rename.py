import os
import re
# import readline

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
    new_episode_format = "{}"

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

    start_episode = int(input("Введите номер начальной серии: "))

    for file in os.listdir(directory):
        if file.endswith(format_files):
            # Извлечь номер эпизода из имени файла
            episode_number_match = re.search(r"\b(\d+)\b", file)
            if episode_number_match:
                episode_number = int(episode_number_match.group(1))
                # Переименование начинается с указанной серии
                if episode_number >= start_episode:
                    # Заменить номер эпизода на нужный формат
                    new_episode_number = new_episode_format.format(str(episode_number).zfill(2))
                    # Заменить или удалить целевую часть имени файла
                    new_name = re.sub(re.escape(target), replacement, file)
                    # Заменить номер эпизода в новом имени файла
                    new_name = re.sub(r"\b(\d+)\b", new_episode_number, new_name)
                    old_path = os.path.join(directory, file)
                    new_path = os.path.join(directory, new_name)
                    print(f"Переименование {old_path} в {new_path}")
                    os.rename(old_path, new_path)

    print("Переименование завершено.")
