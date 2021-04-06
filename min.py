# get 3 digit input from user
# split the 3 digits into a list [1,2,3]
# make sure the 3 digits are different from eachother
# if they are unique then take the input and check if its correct or not
# if the numbers from the input exists in the computers guess (list) then write out close

import random
import pyinputplus as pyip


while True:
    # Get a random 3 digit number in a list from computer
    y = list(range(10))
    random.shuffle(y)
    computer_input = y[:3]

    # Get a user input and put it in user_input variable.
    s = pyip.inputInt(prompt='Enter a number: ', blank=True)
    l = s.split()
    map_object = map(int, l)
    user_input = list(map_object)
    print(user_input)
    # Check if user input is close to computer input.
    check = any(item in user_input for item in computer_input)
    # Check if user input is exactly like computer input.
    # check2 = all(item in user_input for item in computer_input)

    if (user_input == computer_input):
        print("Correct congrats")
        break
    elif (check == True):
        print("Close, right number, but wrong position. Try again...")
    else:
        print("Nope none of the numbers is correct, try again")

    '''
    while len(user_input) < 3:
        number = int(input("Enter a number: "))
        if not 1 <= number <= 9:
            print('Enter a single digit only')
        else:
            user_input.append(number)
    '''

    '''
    for i in range(3):
        y = int(input())
        user_input.append(y)
    '''
