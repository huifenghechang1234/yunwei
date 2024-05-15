"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/22'
code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""
"""
OrganizeIT 2.0

这个自动化脚本可以帮你在几分钟内整理好文件夹。你只需指定需要清理的路径，
本脚本就会根据文件扩展名自动将所有文件划分到不同的文件夹中
"""

import os
import hashlib
import shutil


def get_file_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def organize_and_move_duplicates(folder_path):
    # Create a dictionary to store destination folders based on file extensions
    extension_folders = {}

    # Create the "Duplicates" folder if it doesn't exist
    duplicates_folder = os.path.join(folder_path, 'Duplicates')
    os.makedirs(duplicates_folder, exist_ok=True)

    # Create a dictionary to store file hashes
    file_hashes = {}

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # Get the file extension
            _, extension = os.path.splitext(filename)
            extension = extension.lower()  # Convert extension to lowercase

            # Determine the destination folder
            if extension in extension_folders:
                destination_folder = extension_folders[extension]
            else:
                destination_folder = os.path.join(folder_path,
                                                  extension[1:])  # Remove the leading dot from the extension
                os.makedirs(destination_folder, exist_ok=True)
                extension_folders[extension] = destination_folder

            # Calculate the file hash
            file_hash = get_file_hash(file_path)

            # Check for duplicates
            if file_hash in file_hashes:
                # File is a duplicate, move it to the "Duplicates" folder
                shutil.move(file_path, os.path.join(duplicates_folder, filename))
                print(f"Moved duplicate file {filename} to Duplicates folder.")
            else:
                # Store the file hash
                file_hashes[file_hash] = filename
                # Move the file to the destination folder
                shutil.move(file_path, destination_folder)
                print(f"Moved {filename} to {destination_folder}")


if __name__ == "__main__":
    folder_path = input("Enter the path to the folder to organize: ")
    organize_and_move_duplicates(folder_path)


