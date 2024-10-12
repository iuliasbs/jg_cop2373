# JG
# October 12, 2024
# The program validates user-entered phone number, social security number and zip code

import re

def main():
    phone = input('Enter your phone number: ')

    ssn = input('Enter your Social Security Number: ')

    zip = input('Enter your zip code: ')

    print()

    print('Is the phone number valid?  ' + str(validatePhone(phone)))

    print('Is the Social Security Number valid?  ' + str(validateSsn(ssn)))

    print('Is the phone number valid?  ' + str(validateZip(zip)))

def validatePhone(phone):

    return re.fullmatch(r'^\d{3}-\d{3}-\d{4}$', phone) is not None

def validateSsn(ssn):

    return re.fullmatch(r'^\d{3}-\d{2}-\d{4}$', ssn) is not None

def validateZip(zip):

    return re.fullmatch(r'^\d{5}$', zip) is not None

main()
