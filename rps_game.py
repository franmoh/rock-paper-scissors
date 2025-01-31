import random
game_list = ['rock', 'paper', 'scissor']
computer = c = 0
command = p = 0
print("Score: Computer " + str(c) + " Player " + str(p))
# the loop
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("rock, paper, scissors or quit: ")
    if command == computer_choice:
        print('...Tie...')
    elif command == 'rock':
        if computer_choice == 'scissors':
            print("Player won!")
            p += 1
        else:
            print("Computer won!")
            c += 1
    elif command == 'paper':
        if computer_choice == 'rock':
            print("Player won!")
            p += 1
        else:
            print("Computer won!")
            c += 1
    elif command == 'scissors':
        if computer_choice == 'paper':
            print('Player won!')
            p += 1
        else:
            print("Computer won!")
    elif command == 'Quit':
        break
    else:
        print("Wrong command!")
    print("Player: " + command)
    print("Computer: " + computer_choice)
    print("")
    print("Score: Computer " + str(c) + " Player " + str(p))
    print("")
    
    '''elif p / 2 >= c:
        break
        print("Player won by doubble your score: " + str(p))
    elif c / 2 >= p:
        break
        print("Computer won by double your score: " + str(c))'''
