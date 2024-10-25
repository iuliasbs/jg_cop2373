# JG
# October 24, 2024
# The program creates a CSV file with student grades, reads the file and displays a table

import csv

def save():

    # Prompt the user to enter the number of students
    student_count = int(input('How any students do you want to enter? '))

    # Open the CSV file for writing
    with open('grades.csv', mode='w', newline='') as file:

        # Create a writer for the file
        writer = csv.writer(file)

        # Write a header row to the CSV file
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # For each student Prompt the user to enter the name and 3 grades
        for i in range(0, student_count):

            first_name = input("First Name: ")

            last_name = input("Last Name: ")

            grade_1 = int(input("First Grade: "))

            grade_2 = input("Second Grade: ")

            grade_3 = input("Third Grade: ")

            # Write the student's information to the CSV file
            writer.writerow([first_name, last_name, grade_1, grade_2, grade_3])

def read():
    # Open the CSV file for read
    with open('grades.csv', mode='r') as file:

        # Create a reader for the file
        reader = csv.reader(file)

        # Read the hader row
        headers = next(reader)

        # Print the hader row
        print(format(headers[0], '15') + format(headers[1], '15') + format(headers[2], '10') + format(headers[3], headers[4], '10'))

        # Read each row in the file
        for row in reader:

            #Print the row
            print(format(row[0], '15') + format(row[1], '15') + format(row[2], '10') + format(row[3], '10') + format(row[4], '10'))

def main():

    save()

    read()

main()