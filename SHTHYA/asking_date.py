# -*- coding: utf-8 -*-
"""
Author: George Bitsonis
"""

from datetime import datetime
from calendar import monthrange

# def asking_date():
    # """ Asking the user for the desired date with the current date as default.
        # and returning a tuple with the weeknumber and the monthnumber.
    # """

    # user_input = input(
        # f"The current date is: {datetime.now().strftime('%m-%Y')}, \n"
        # "Do you want another date? (Y/N) "
    # )

    # if user_input.lower() == "y" or user_input.lower() == "yes":
        # user_input_year = int(input("Enter the year: "))
        # user_input_month = int(input("Enter the month: "))

        # try:
            # days_of_month = monthrange(user_input_year, user_input_month)
        # except Exception as e:
            # print(e)
            # days_of_month = asking_date()
    # elif user_input.lower() == "n" or user_input.lower() == "no":
        # days_of_month = monthrange(datetime.now().year, datetime.now().month)

    # else:
        # print("Not a valid response!")
        # days_of_month = asking_date()

    # return days_of_month  # Returning a tuple, where we need the second element.



def asking_date():
    """ Asking the user for the desired date with the current date as default,
        returning a set with: a tuple with the weeknumber and the monthnumber, the month and the wear.
    """

    user_input = input(
        f"The current date is: {datetime.now().strftime('%m-%Y')}, \n"
        "Do you want another date? (Y/N) "
    )

# CAUTION, an infinate loop may arise, if the user does not pass an acceptable answer!
    if user_input.lower().strip() == "y" or user_input.lower().strip() == "yes":

              user_input_year = int(input("Enter the year: "))
              user_input_month = int(input("Enter the month: "))

              try:
                     days_of_month = monthrange(user_input_year, user_input_month)

              except Exception as e:
                     days_of_month = asking_date()

              return (days_of_month, f'{user_input_month}'.zfill(2), user_input_year)

    elif user_input.lower().strip() == "n" or user_input.lower().strip() == "no":

              days_of_month = monthrange(datetime.now().year, datetime.now().month)
              return (days_of_month, datetime.now().month, datetime.now().year)
    else:
              print("Not a valid response!")
              days_of_month = asking_date()



if __name__ == '__main__':
     print(asking_date())
