# JG
# October 12, 2024
# The program validates user-entered phone number, social security number and zip code

import re

def main():

    # Create the pattern to look for
    pat = r'[A-Z0-9].*?[.!?](?! [a-z]|\w)'

    # Create the string with all of the sentences
    s = '''See the U.S.A. today. 5It's right here, not a world away. Average temp. is 70.5. It's fun!'''

    # Create the list of sentences
    m = re.findall(pat, s, flags=re.DOTALL)

    # Loop through the list of sentences
    for i in m:

        # Print the sentence
        print('->', i)

    # Print the number of sentences
    print('There are ' + str(len(m)) + ' sentences')

main()
