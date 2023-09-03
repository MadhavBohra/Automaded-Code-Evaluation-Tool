import os
import zipfile
import shutil
# from rename import change_file_names_in_folders




def delete_empty_folders(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)



def move_files_to_outermost_folder(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            source_path = os.path.join(root, file_name)
            destination_path = os.path.join(directory, file_name)
            shutil.move(source_path, destination_path)


def zip_extractor(zip_file_path,output_directory):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        print(zip_file)
        zip_file.extractall(output_directory)
    for file_name in os.listdir(output_directory):
        file_path = os.path.join(output_directory,file_name)
        if file_name.endswith(".zip"):
            file_name = file_name.replace(".zip","")
            with zipfile.ZipFile(file_path, 'r') as zip_file:
                zip_file.extractall(f"{output_directory}/{file_name}")
            os.remove(file_path)
    for file_name in os.listdir(output_directory):
        file_path = os.path.join(output_directory,file_name)
        move_files_to_outermost_folder(file_path)

    delete_empty_folders(output_directory)
    # change_file_names_in_folders(output_directory)
        


# Example usage
# zip_file_path = 'Input Folder\Student Submissions\ORANGE_SET.zip'
# output_directory = 'test03'

# zip_extractor(zip_file_path, output_directory)
