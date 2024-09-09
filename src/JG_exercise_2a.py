# JG
# September 9, 2024
# The program calculates the spam score of a message

def main():
    SPAM_WORDS = [
        "Congratulations!",
        "You've won",
        "Click here",
        "Act now",
        "Limited time offer",
        "100% free",
        "Risk-free",
        "Earn money fast",
        "Make money online",
        "Exclusive deal",
        "Unsecured credit",
        "Free gift",
        "Guarantee you’ll win",
        "Increase your income",
        "No cost",
        "Urgent response needed",
        "Call now",
        "Get paid",
        "Free trial",
        "Money-back guarantee",
        "Win big",
        "Special promotion",
        "Amazing opportunity",
        "Be your own boss",
        "Last chance",
        "Save big",
        "Act fast",
        "Click below",
        "This isn't a scam",
        "Free access"
    ]

    # Ask the user to enter the email message
    message = input("Enter your email message: ")

    # Create an empty list for tracking the spam words found
    spam_found = []

    # Loop through the spam words
    for word in SPAM_WORDS:

        # If the message contains the spam word, add it to the list of spam found
        if word.lower() in message.lower():

            spam_found.append(word)

    # Count how many spam words were found
    spam_score = len(spam_found)

    # Display the spam score
    print("The email message contains " + str(spam_score) + " spam words or phrases.")

    # Calculate the likelihood that the message is spam
    if spam_score > 3:

        spam_likelihood = "Very high"

    elif spam_score > 2:

        spam_likelihood = "High"

    elif spam_score > 1:

        spam_likelihood = "Medium"

    elif spam_score > 0:

        spam_likelihood = "Low"

    else:

        spam_likelihood = "Very Low"

    # Dispay the likelihood that the message is spam
    print("The likelihood that the email message is spam is " + spam_likelihood)

main()
