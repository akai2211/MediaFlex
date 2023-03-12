import os
import ffmpeg
# import readline

# путь к директории
dir_path = input("Путь к директории (или q для выхода): ")

if dir_path.lower() == 'q':
    exit()

# формат файлов, из которых нужно извлекать аудио
input_format = '.' + input('Из какого формата извлекать аудио?: ')

# количество проверенных файлов и количество файлов с аудио-дорожками
total_files = 0
audio_files = 0
codec_counts = {}

# цикл по всем файлам с нужным расширением в директории
for file_name in os.listdir(dir_path):
    if file_name.endswith(input_format):
        file_path = os.path.join(dir_path, file_name)
        # получение информации о файле
        probe = ffmpeg.probe(file_path)
        # получение информации об аудио-дорожках в файле
        audio_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'audio']
        # вывод формата каждой аудио-дорожки
        if len(audio_streams) > 0:
            for audio_stream in audio_streams:
                codec_name = audio_stream['codec_name']
                if codec_name in codec_counts:
                    codec_counts[codec_name] += 1
                else:
                    codec_counts[codec_name] = 1
            audio_files += 1
        else:
            print('Аудио-дорожки не найдены в файле', file_name)
        total_files += 1

# вывод общего количества проверенных файлов и файлов с аудио-дорожками
print('Файлов с аудио-дорожками:', audio_files)

if len(codec_counts) > 0:
    for codec_name, count in codec_counts.items():
        print(f'{codec_name}:{count}', end=', ')
    print()
else:
    print('Нет аудио-дорожек')

print('Проверено файлов:', total_files)
