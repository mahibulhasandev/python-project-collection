# Loop 
    # Ask: rool the dice?
    # If user enters y
    #       generate who random numbers
    #       print them
    # if user enters next
    #      print thank you message 
    #      Terminate 
    # Else 
    #      print invalid choise 


import random

while True:
    choise = input('Roll the dice? (y/n): ').lower()
    if choise == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choise == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')