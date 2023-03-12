import os

# Сменить рабочую директорию на директорию содержащую файлы
os.chdir('/home/akai/Документы/MediaFlex/tests/SUB/')

# Цикл по всем файлам в директории
for filename in os.listdir('.'):
    # Разделить имя файла на базовое имя и расширение
    basename, extension = os.path.splitext(filename)
    # Проверить, является ли расширение заглавным
    if extension.islower(): # islower isupper
        # Преобразовать расширение в строчные буквы
        new_extension = extension.upper() # upper lower
        # Переименовать файл с новым расширением
        os.rename(filename, basename + new_extension)


    # # Цикл по всем файлам в директории
    # for filename in os.listdir('.'):
    #     # Разделить имя файла на базовое имя и расширение
    #     basename, extension = os.path.splitext(filename)
    #     # Проверить, является ли расширение заглавным
    #     if extension.isupper():
    #         # Преобразовать расширение в строчные буквы
    #         new_extension = extension.lower()
    #         # Переименовать файл с новым расширением
    #         os.rename(filename, basename + new_extension)