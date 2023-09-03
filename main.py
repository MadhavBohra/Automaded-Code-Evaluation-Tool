import os
from result_case_generator import result_case_generator
from zip_extractor import zip_extractor
from solution_evaluator import solution_evaluator
from create_student_marks_csv import create_student_marks_csv
from evaluate import evaluate
from model_train import train_gpt_model
from rename import rename_and_copy
import time

# Take input of Sets
# Take input of Test Cases
# Take input of Submissions

def main():
    # First Generate the Result Cases
    # Then Evaluate

    # Looping through each and every set :


    # Path Defined here : 

    current_directory = os.getcwd()
    solutions_path = os.path.join(current_directory,"Input Folder\Correct Solution")
    testcases_path = os.path.join(current_directory,"Input Folder\TestCases")
    resultcases_path = os.path.join(current_directory,"Output Folder\ResultCases")
    solutions_folder = os.listdir(solutions_path)
    testcases_folder = os.listdir(testcases_path)
    resultcases_folder = os.listdir(resultcases_path)
    resultcases_admin_path = os.path.join(current_directory,"Output Folder\ResultCases_For_Admin")

    # Initializing paths : 

    # Generating Result Cases
    

    for solution_set_folder,testcase_set_folder,resultcase_set_folder in zip(solutions_folder,testcases_folder,resultcases_folder):
        script_directory = os.path.join(solutions_path,solution_set_folder)
        testcase_path = os.path.join(testcases_path,testcase_set_folder)
        resultcase_path = os.path.join(resultcases_path,resultcase_set_folder)
        resultcase_admin_path = os.path.join(resultcases_admin_path,resultcase_set_folder)
        for input_argument in range(1,4):
            result_case_generator(script_directory,testcase_path,resultcase_path,resultcase_admin_path,input_argument)



# # Extracting Files :

    zip_files_path = os.path.join(current_directory,"Input Folder\Student Submissions")
    extracted_files_path = os.path.join(current_directory,"Output Folder/Student Submissions")

    for zip_file in os.listdir(zip_files_path):
        input_file_path = os.path.join(zip_files_path,zip_file)
        extracted_file = zip_file.replace(".zip","")
        output_file_path = os.path.join(extracted_files_path,extracted_file)
        zip_extractor(input_file_path,output_file_path)

# # Renaming Files : 
    
    submission_path = os.path.join(current_directory,"Output Folder/Student Submissions")
    for submission_set,correct_solution_set in zip(os.listdir(submission_path),os.listdir(solutions_path)):
        submission_set_path = os.path.join(submission_path,submission_set)
        correct_set_path = os.path.join(solutions_path,correct_solution_set)
        for IDnumber in os.listdir(submission_set_path):
            submission = os.path.join(submission_set_path,IDnumber)
            rename_and_copy(submission,correct_set_path)




# #     # Training GPT Model :

    prompt_folder = os.path.join(current_directory,"Input Folder/Prompt Folder")
    output_response_folder = os.path.join(current_directory,"Output Folder/Responses")

    for prompt_set,response_set in zip(os.listdir(prompt_folder),os.listdir(output_response_folder)):
        prompt_path = os.path.join(prompt_folder,prompt_set)
        response_path = os.path.join(output_response_folder,response_set)
        for i in range(1,3):

            train_gpt_model(prompt_path,response_path,i)




#     # Evaluating The Submissions : 
    
    student_submission_files_path = os.path.join(current_directory,"Output Folder/Student Submissions")
    

    for set in os.listdir(student_submission_files_path):
        response_path = os.path.join(current_directory,f"Output Folder/Responses/{set}")
        set_path = os.path.join(student_submission_files_path,set)
        for submission_folder in os.listdir(set_path):
            script_directory = os.path.join(set_path,submission_folder)
            print(script_directory)
            # Evaluating all 3
            student_data = []
            for input_argument in range(1,4):
                checking_testcases_path = os.path.join(testcases_path,f"{set}/testcases{input_argument}.txt")
                checking_resultcases_path = os.path.join(resultcases_path,f"{set}/resultcases{input_argument}.txt")
                answer = solution_evaluator(script_directory,checking_testcases_path,checking_resultcases_path,input_argument)
                if answer:
                    if input_argument == 1:
                        student_data.append((1,20))
                    elif input_argument == 2:
                        student_data.append((2,30))
                    else:
                        student_data.append((3,30))
                else:
                    
                    student_data.append([input_argument,0])
                    if input_argument == 3:
                        continue
                    else:
                        evaluate(response_path,script_directory,input_argument)
                        # continue
            
            create_student_marks_csv(f"{script_directory}/Output Marks.csv",student_data)
            time.sleep(1)


main()