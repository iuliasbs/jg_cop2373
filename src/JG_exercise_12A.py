# JG
# November 24, 2024
# The program calculates and prints statistics for exam grades

import numpy as np

def main():

    dt = [('First Nmae', 'U10'), ('Last Nmae', 'U10'), ('Exam 1', 'f4'), ('Exam 2', 'f4'), ('Exam 3', 'f4')]

    # Load the data from the CSV file into a numpy array
    data = np.loadtxt('grades.csv', dt, delimiter=',', encoding=None, skiprows=1)

    # Print the first few rows of the dataset
    print("First few rows of the dataset:")

    print(data[0])

    print(data[1])

    print(data[2])

    # Make a numpy array with the exam scores
    exam_scores = np.array([data['Exam 1'], data['Exam 2'], data['Exam 3']])

    # Calculate and display statistics for each exam
    for i, exam in enumerate(['Exam 1', 'Exam 2', 'Exam 3']):

        print(f"\nStatistics for {exam}:")

        print(f"Mean: {np.mean(exam_scores[:, i])}")

        print(f"Median: {np.median(exam_scores[:, i])}")

        print(f"Standard Deviation: {np.std(exam_scores[:, i])}")

        print(f"Minimum: {np.min(exam_scores[:, i])}")

        print(f"Maximum: {np.max(exam_scores[:, i])}")

    # Calculate and display statistics for all exams
    all_grades = exam_scores.flatten()

    print("\nOverall statistics across all exams:")

    print(f"Mean: {np.mean(all_grades)}")

    print(f"Median: {np.median(all_grades)}")

    print(f"Standard Deviation: {np.std(all_grades)}")

    print(f"Minimum: {np.min(all_grades)}")

    print(f"Maximum: {np.max(all_grades)}")


    # Calculate and display the number of students who passed and failed each exam
    passing_grade = 60

    for i, exam in enumerate(['Exam 1', 'Exam 2', 'Exam 3']):

        pass_count = np.sum(exam_scores[:, i] >= passing_grade)

        fail_count = exam_scores.shape[0] - pass_count

        print(f"\n{exam} - Passed: {pass_count}, Failed: {fail_count}")


    # Calculate and display overall pass percentage across all exams
    total_passed = np.sum(exam_scores >= passing_grade)

    total_students = exam_scores.size

    pass_percentage = (total_passed / total_students) * 100

    print(f"\nOverall pass percentage across all exams: {pass_percentage:.2f}%")


# Call the main function
main()