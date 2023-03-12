import os
import ffmpeg
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

    output_folder = input_folder + 'files/'
    input_format_files = '.' + input('Из какого формата конвертировать файлы?: ')
    output_format_files = '.' + input('В какой формат конвертировать файлы?: ')

    # создание выходной папки, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # получение списка файлов во входной папке
    files = os.listdir(input_folder)

    for file in files:
        # проверка, что это видео файл
        if file.endswith(input_format_files):
            # формирование путей входного и выходного файлов
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + output_format_files)

            # конвертация видео
            (
                ffmpeg
                .input(input_path)
                .output(output_path)
                .run()
            )

    print('Конвертация завершина.')
