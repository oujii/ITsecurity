# get 3 digit input from user
# split the 3 digits into a list [1,2,3]
# make sure the 3 digits are different from eachother
# if they are unique then take the input and check if its correct or not
# if the numbers from the input exists in the computers guess (list) then write out close

import random


while True:
    computer_input = [1, 2, 3]
    # Get a random input from the computer and put it in the computer_input variable.
    # y = list(range(10))
    # random.shuffle(y)
    # computer_input = y[:3]

    try:
        # Get a user input and put it in user_input variable.
        s = input("Enter 3 digits with a space between\n")
        l = s.split()
        map_object = map(int, l)
        user_input = list(map_object)

    except ValueError:
        print(f'ERROR: You need to enter a number')
    else:
        # Check if user input is close to computer input.
        check = any(item in user_input for item in computer_input)
        if (user_input == computer_input):
            print("Correct congrats")
            break
        elif (check == True):
            print("Close, right number(s), but wrong position. Try again...")
        else:
            print("Nope none of the numbers is correct, try again")
