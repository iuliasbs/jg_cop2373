# JG
# August 28, 2024
# The program simulates a Magic 8 Ball

import random

# This function creates the 8ball_responses.txt file and adds the possible answers to it.
def create_answers():

    lines = [
        "Yes, of course!\n",
        "Without a doubt, yes.\n",
        "You can count on it.\n",
        "For sure!\n",
        "Ask me later! \n",
        "I'm not sure. \n",
        "I can't tell you right now. \n",
        "I'll tell you after my nap. \n",
        "No way!\n",
        "I don't think so. \n",
        "Without a doubt, no. \n",
        "The answer is clearly NO!\n"
    ]

    file = open('8ball_responses.txt', 'w')
    file.writelines(lines)

# This function reads the 8ball_responses.txt file and returns the lines as an array of strings.
# The function returns an array of strings with the possible answers
def get_answers():

    file = open('8ball_responses.txt', 'r')

    return file.readlines()

# This function runs the program.
def main():

    # Create the answers file
    create_answers()

    # Load the answers file into an array
    answers = get_answers()

    # Start the loop
    while True:

        # Prompt the user for their question
        question = input('Ask the Magic 8 Ball a yes/no question. Type "quit" to quit.\n')

        # If the user typed quit, break from the loop
        if (question == 'quit'):
            
            break
            
        else:

            # Else print a random answer from the array
            print(random.choice(answers))

main()
