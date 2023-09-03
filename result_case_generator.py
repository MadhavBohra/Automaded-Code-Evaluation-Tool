import subprocess
import os


def result_case_generator(script_directory,testcases_path,resultcases_path,resultcases_admin_path,input_argument):

    with open(f"{testcases_path}/testcases{input_argument}.txt","r") as test_file:
        test_cases = test_file.read().splitlines()

    with open(f"{resultcases_path}/resultcases{input_argument}.txt","w") as file:
        file.truncate()

    output_for_admin = ""
    for test_case in test_cases:

        
        process = subprocess.Popen(
            ["bash",f"myScript.sh",f"{input_argument}"],
            cwd=str(script_directory),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(test_case)
        output_for_admin += "TEST CASE : \n\n"
        output_for_admin += f"{test_case}\n\n"
        output_for_admin += "---------------------------------------\n\n"
        process.stdin.write(f"{test_case}")
        process.stdin.close()
        output = process.stdout.read()
        
        
        
        if output == "":
            output = " \n"

        temp_output = output
        temp_output = temp_output.replace(": ",": \n")
        temp_output = temp_output.replace(":",":\n")
        output_for_admin += "CONSOLE OUTPUT : \n"
        output_for_admin += temp_output
        output_for_admin += "\n\n----------------------------------------------\n\n"
        with open(f"{resultcases_path}/resultcases{input_argument}.txt", "a") as output_file:

            output_file.write(output)
        print(output)
    with open(f"{resultcases_admin_path}/resultcases{input_argument}.txt","w") as file:
        file.write(output_for_admin)


# current_directory = os.getcwd()

# # Specify the folder you want to work in (e.g., "my_folder")
# target_folder = "Solutions\Solutions\Set1-ORANGE"

# # Merge the current directory path with the target folder
# target_directory = os.path.join(current_directory, target_folder)
# print(target_directory)

# result_case_generator(target_directory,"testcase2_ORANGE.txt",2)
