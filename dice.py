import random
want_to_quit = '' # Empty string are false
while not want_to_quit:
    dice_value = random.randint(1,6)
    # Second dice value
    dice_value_two = random.randint(1,6)
    # The value for each of the rolled dice
    print(f'You rolled a {dice_value} and a {dice_value_two}')
    # Both values are equal thus another turn
    if dice_value == dice_value_two:
        print('Both dice are the same, you get another turn.')
    # Since the dice match then we try again
    else:
    # Not typing anything and pressing enter will set want_to_quit to an empty string
        want_to_quit = input('Press enter to roll again, any other key to quit')
    