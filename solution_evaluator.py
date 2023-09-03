import subprocess
import os
import time



def solution_evaluator(script_directory,testcases_path,resultcases_path,input_argument):
    
    final_output = ""
    output_for_the_textfile = ""
    print("Running:")

    with open(str(testcases_path), "r") as test_file, open(str(resultcases_path), "r") as result_file:
        test_cases = test_file.read().splitlines()
        result_cases = result_file.read()
        

    for test_case in test_cases:
        # Create a subprocess and pass the test case as input
        process = subprocess.Popen(
            ["bash", "myScript.sh", str(input_argument)],
            cwd=str(script_directory),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        output_for_the_textfile += "TEST CASE:\n\n"
        output_for_the_textfile += f"{test_case}\n\n"
        output_for_the_textfile += "-------------------------------------------------\n"
        output_for_the_textfile += "CONSOLE OUTPUT:\n"
        


        # Communicate with the subprocess by passing the test case as input
        
        try:
            output, error = process.communicate(str(test_case), timeout=30)

            output_for_the_textfile += output.replace(": ",": \n")
            output_for_the_textfile += "\n"
            output_for_the_textfile += f"{error}\n"
            output_for_the_textfile += "-------------------------------------------------\n"
        except subprocess.TimeoutExpired:
            # Terminate the process if it exceeds the timeout
            process.terminate()
            process.wait()  # Wait for the process to be terminated
            print("Subprocess exceeded timeout of 30 seconds.")
            output = "Time Limit Exceeded, Infinite Loop"
            output_for_the_textfile += "\n"
            output_for_the_textfile += f"{output}\n"
            output_for_the_textfile += "--------------------------------------------------\n"

            with open(f"{script_directory}/CONSOLE_LOG{input_argument}.txt",'w') as output_text_file:
                output_text_file.write(f"{output_for_the_textfile}\n")
            print("Wrong")
            return False


        
        if output == "":
            output = " \n"
        print(test_case)
        print(output)
        final_output += output
        

    if(final_output == result_cases):
        with open(f"{script_directory}/CONSOLE_LOG{input_argument}.txt",'w') as output_text_file:
                output_text_file.write(f"{output_for_the_textfile}\n")
        print("Correct")
        return True
    else:
        with open(f"{script_directory}/CONSOLE_LOG{input_argument}.txt",'w') as output_text_file:
                output_text_file.write(f"{output_for_the_textfile}\n")
        print("Wrong")
        return False


        

    

# current_directory = os.getcwd()

# # Specify the folder you want to work in (e.g., "my_folder")
# target_folder = "Output Folder/Student Submissions/2022A2PS1103P/2022A2PS1103P"

# # Merge the current directory path with the target folder
# target_directory = os.path.join(current_directory, target_folder)
# print(target_directory)

# solution_evaluator(target_directory,"Input Folder/TestCases/Set1/testcases1.txt","Output Folder/ResultCases/Set1/resultcases1.txt",1)
