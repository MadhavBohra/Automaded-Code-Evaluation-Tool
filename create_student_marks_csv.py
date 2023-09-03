import csv

def create_student_marks_csv(file_path, student_data):
    # student_data should be a list of tuples containing (ID, Marks) pairs

    # Open the CSV file in write mode
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Question Number', 'Marks'])

        # Write the student data rows
        writer.writerows(student_data)