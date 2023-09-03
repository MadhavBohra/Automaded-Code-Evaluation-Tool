import pandas as pd
import os
import csv

def marks_reader(file_path,ID,set_number):
    if set_number == "SET1":
         set_number = "SET1_ORANGE"
    if set_number == "SET2":
         set_number = "SET2_PINK"
    if set_number == "SET3":
         set_number = "SET3_YELLOW"
    data = pd.read_csv(f"{file_path}/Output Marks.csv")
    total_marks = int(data['Marks'][0])+int(data['Marks'][1])+int(data['Marks'][2])
    output_data = [ID,set_number,"",data['Marks'][0],"",data['Marks'][1],"",data['Marks'][2],total_marks]
    return output_data



current_directory = os.getcwd()
submission_path = os.path.join(current_directory,"Output Folder/Student Submissions")


marks = []

for sets in os.listdir(submission_path):
    submission_set_path = os.path.join(submission_path,sets)
    for IDnumber in os.listdir(submission_set_path):
        script_directory = os.path.join(submission_set_path,IDnumber)
        marks.append(marks_reader(script_directory,IDnumber,sets))

file_path = os.path.join(current_directory,"Output Folder/Final Marks.csv")
with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['ID', 'SET','Question One Code Correctness','Question One Output Marks','Question Two Code Correctness','Question Two Output Marks','Question Three Code Correctness','Question Three Output Marks','Total Marks'])

        # Write the student data rows
        writer.writerows(marks)