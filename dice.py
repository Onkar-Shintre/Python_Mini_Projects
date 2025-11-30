import random 

again = True

while again :
    print(random.randint(1, 6))  #Number
    another_roll = input("Want to roll the dice again? (yes/no):")
    if another_roll.lower() == "yes":
        continue
    else:
        break

    
