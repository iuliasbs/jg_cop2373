# JG
# September 22, 2024
# This program will ask the user for their monthly expenses and display the lowest, highest, and total expense.
import functools


def main():

    #Create an array for the amounts.
    expenses = []

    #Create the loop.
    while True:

        #Create the input for the type of monthly expense.
        type = input("Enter the type of monthly expense. When finished, type QUIT")

        #Create the condition for ending the loop.
        if type == "QUIT":

            break

        #Create the input for the amount.
        amount = int(input("Enter the expense amount"))

        #Add the amount to the array
        expenses.append(amount)

    #Print the total amount.
    print(functools.reduce(lambda total, current: total + current, expenses))

    #Print the lowest amount.
    print("Lowest value is " + str(functools.reduce(lambda lowest, current: lowest if lowest < current else current, expenses)))

    #Print the largest amount.
    print("Largest value is " + str(functools.reduce(lambda largest, current: largest if largest > current else current, expenses)))








main()