"""
Скрипт для автоматического удаления всех файлов в нужной директории
"""


import os
import shutil


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
        print(f"Нет такого пути: {path}")
        get_path_for_clean()


def remove_all_files(path):
    all_items = [os.path.join(path, item) for item in os.listdir(path)]
    files = [file for file in all_items if os.path.isfile(file)]
    dirs = [d for d in all_items if os.path.isdir(d)]

    print(f"В данном каталоге {len(files)} и {len(dirs)} директорий")

    confirm = input("\nУдалить ВСЁ содержимое? (y/n): ")

    if confirm.lower() == "y":
        for file in files:
            print(f"Удаляем файл: {os.path.basename(file)}")
            os.remove(file)
        else:
            print("Все файлы удалены!")

        for dir in dirs:
            shutil.rmtree(dir)
            print(f"Удалена директория: {os.path.basename(dir)}")
        else:
            print("Все директории удалены!")

    print("\nУдаление прошло успешно!")


if __name__ == "__main__":
    get_path_for_clean()
