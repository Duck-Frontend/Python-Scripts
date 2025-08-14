"""
Скрипт для автоматического удаления всех файлов в нужной директории
"""


import os


def get_path_for_clean():
    print(f"Текущая директория: {os.getcwd()}")
    directories = [d for d in os.listdir() if os.path.isdir(d)]
    print("Доступные директории:", ", ".join(directories))

    path = input("\nВведите имя директории для отчистки: ")
    abs_path = os.path.abspath(path)

    if os.path.exists(path):
        print("Начинаю отчистку")
        remove_all_files(abs_path)
    else:
        print("Нет такого пути")


def remove_all_files(path):
    os.chdir(path)
    files = os.listdir()

    for file in files:
        print(file, sep=",", end=" ")

    answer = int(input("\nУдалить все эти файлы?\n1: Да 2: Нет\n: "))

    if answer == 1:
        for file in files:
            os.remove(file)
        else:
            print("Все Файлы удалены")

    else:
        print("Всего хорошего!")


get_path_for_clean()
