import os
import shutil
import time

def main():

    deleted_folders_count = 0
    deleted_files_count = 0

    path = "/PATH_TO_DELETE"

    days = 30

    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):


     for root_folder, folders, files in os.walk(path):

        if seconds >= get_files_or_folders_age(root_folder):

           os.remove_folder(root_folder)
           deleted_folders_count += 1

           break

        else:

            for folder in folders():

                folder_path = os.path.join(root_folder,folder)

                if seconds >= get_file_or_folder_age(folder_path):

                 os.remove_folder(root_folder)
                 deleted_folders_count += 1

            for files in files():

                files_path = path.join(root_folder, files)

                if seconds >= get_files_or_folders_age(files_path):

                 os.remove_files(files_path)
                 deleted_folders_count += 1

    else:

                if seconds >= get_files_or_folders_age(path):

                    os.remove_files(path)
                    deleted_files_count += 1
            



       
