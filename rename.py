import os
import shutil



def rename_and_copy(submission_path,source_directory):

    # Rename Task
    file_names = os.listdir(submission_path)
    for file_name in file_names:
        if file_name.startswith("f1") and file_name.endswith(".c"):
            old_file_path = os.path.join(submission_path,file_name)
            new_file_path = os.path.join(submission_path,"f1.c")
            if not os.path.exists(new_file_path):
                os.rename(old_file_path, new_file_path)
            
        if file_name.startswith("f2") and file_name.endswith(".c"):
            old_file_path = os.path.join(submission_path,file_name)
            new_file_path = os.path.join(submission_path,"f2.c")
            if not os.path.exists(new_file_path):
                os.rename(old_file_path, new_file_path)
            
        if file_name.startswith("f3") and file_name.endswith(".c"):
            old_file_path = os.path.join(submission_path,file_name)
            new_file_path = os.path.join(submission_path,"f3.c")
            if not os.path.exists(new_file_path):
                os.rename(old_file_path, new_file_path)

    # Copy Task :
    files_to_copy = [
    "f1.h",
    "f2.h",
    "f3.h",
    "main.c",
    "myScript.sh",
    # Add more file names here if needed
    ]

    for file_name in files_to_copy:
        file_path = os.path.join(source_directory, file_name)
        shutil.copy2(file_path, submission_path)

    