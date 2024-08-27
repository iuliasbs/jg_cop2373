# JG
# August 27, 2024
# The program will pre-sell a limited number of cinema tickets. The program executes a loop until all tickets are sold. Each buyer is allowed to purchase up to 4 tickets. The program ends when all tickets have been sold. This software would allow a ticket company to pre-sell tickets to concerts and other events.

def main():

    # Greet the user
    print('Welcome to the ticket market. We have 20 tickets available. Each buyer can purchase up to 4 tickets.')

    # Initialize the variables
    tickets_left = 20

    buyers = 0

    # Start the loop and check the loop condition
    while (tickets_left > 0):

        # Prompt the user for how many tickets they will purchase
        purchased = int(input('How many tickets would you like to purchase? '))

        # Warn the user if they tried to purchase more than 4
        if (purchased > 4):

            print('I am sorry, but each buyer can purchase up to 4 tickets.')

        else:

            # Warn the user if they tried to purchase more tickets than are available
            if (purchased > tickets_left):

                print('I am sorry, but we only have ' + str(tickets_left) + ' left. I will sell them all to you.')

                purchased = tickets_left

            # Process the purchase and subtract the number purchased from the available count
            tickets_left -= purchased

            # Increment the total number of buyers
            buyers += 1

            # Print how many tickets are left
            print('There are ' + str(tickets_left) + ' tickets left')

    # After the loop is finished, print a summary including the total number of buyers
    print('All tickets have been sold!')

    print('There were ' + str(buyers) + ' buyers')

main()
