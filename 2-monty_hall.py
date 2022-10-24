import random


def monty_hall(attemps):
    """ Monty Hall problem simulation. """
    choice_changed = []
    choice_stay = []

    for i in range(0, attemps):
        # Car behind door 1, 2 or 3
        prize = random.choice(['Door 1', 'Door 2', 'Door 3'])
        # Player choice a random door
        player_choice = random.choice(['Door 1', 'Door 2', 'Door 3'])
        # Monty Hall open a door with a goat
        monty_hall_choice = list({'Door 1', 'Door 2', 'Door 3'} - {player_choice, prize})[0]
        # Other door different of player choice and Monty Hall choice
        other_door = list({'Door 1', 'Door 2', 'Door 3'} - {player_choice, monty_hall_choice})[0]
        # Case 1:  Player change his choice to the other door and win
        choice_changed.append(other_door == prize)
        # Case 2:  Player stay with his choice and win
        choice_stay.append(player_choice == prize)

    print(f'\n\
    {attemps:,} games were played \n\
    Chances of winning if you change your choice: {"{:.2%}".format(sum(choice_changed) / attemps)} \n\
    Chances of winning if you stay with your choice {"{:.2%}".format(sum(choice_stay) / attemps)}')


def one_more_door(attemps):
    """ Add a door to Monty Hall problem simulation. """
    choice_changed = []
    choice_stay = []
    monty_win = []

    for i in range(0, attemps):
        # Car behind door 1, 2, 3 or 4
        prize = random.choice(['Door 1', 'Door 2', 'Door 3', 'Door 4'])
        # Player choice a random door
        player_choice = random.choice(['Door 1', 'Door 2', 'Door 3', 'Door 4'])
        # Monty Hall open a random door
        monty_hall_choice = random.choice(
            list({'Door 1', 'Door 2', 'Door 3', 'Door 4'} - {player_choice}))

        if monty_hall_choice != prize:
            # Other doors different of player choice and Monty Hall choice
            other_door_1 = list({'Door 1', 'Door 2', 'Door 3', 'Door 4'} - {player_choice, monty_hall_choice})[0]
            other_door_2 = list({'Door 1', 'Door 2', 'Door 3', 'Door 4'} - {player_choice, monty_hall_choice})[1]

            # Case 1:  Player change his choice to the other doors and win
            choice_changed.append(other_door_1 == prize or other_door_2 == prize)
            # Case 2:  Player stay with his choice and win
            choice_stay.append(player_choice == prize)

        # Case 3:  Monty Hall open the door with the car
        monty_win.append(monty_hall_choice == prize)

    print(f'\n\
    {attemps:,} games were played \n\
    Chances of winning if you change your choice: {"{:.2%}".format(sum(choice_changed) / attemps)} \n\
    Chances of winning if you stay with your choice {"{:.2%}".format(sum(choice_stay) / attemps)} \n\
    Chances of winning if Monty Hall open the door with the car {"{:.2%}".format(sum(monty_win) / attemps)}')


if __name__ == '__main__':
    monty_hall(100000)
    monty_hall(1000000)
    print('_______________________________________________________________________________________________ \n\
            Now we add a door to the game.')
    one_more_door(100000)
    one_more_door(1000000)
