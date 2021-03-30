import random

computer_choice = random.choice(["sten", "sax", "påse"])

user_choice = input("Sten sax påse?\n")

if computer_choice == user_choice:
    print("Lika!")
elif user_choice == "sten" and computer_choice == "sax":
    print("Du vann")
elif user_choice == "påse" and computer_choice == "sten":
    print("Du vann")
elif user_choice == "sax" and computer_choice == "påse":
    print("Du vann")
else:
    print("Du förlorade")
