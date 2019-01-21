"""
Ky Kartchner
CS 1400-1
Assignment 7

task2: Simulates the "Three Doors" games, proving Marilyn vos Savant's proposal that it is in one's best interest to
switch to the other door each time instead of keeping their initial pick.
"""
import random
PLAY_TIMES = 100000
wins = 0

will_switch = True if \
    input("Would you like to switch from your initial pick to the other remaining door each round? (Y/N): ") == "Y"\
    else False

for i in range(0, PLAY_TIMES):
    revealable_doors = [1, 2, 3]                            # Set revealable doors to include  all doors

    prize_door = random.randint(1, 3)                       # Randomly place car behind one of the doors
    revealable_doors.remove(prize_door)                     # Remove prize door from revealable doors

    player_pick = random.randint(1, 3)                      # Randomly pick player's initial door

    if player_pick != prize_door:                           # The same door cannot be removed twice from the list so
        revealable_doors.remove(player_pick)                # only remove if player's pick is not the prize door

    index = random.randrange(0, len(revealable_doors))      # Pick a random "revealable door" to reveal
    del(revealable_doors[index])                            # It has now been revealed so remove it from the list

    if player_pick == prize_door:                           # The "switch to" door is either the prize door or the
        switch_door = revealable_doors[0]                   # remaining revealable door
    else:
        switch_door = prize_door

    if will_switch:                                         # Set player's pick to the "switch to" door if they chose
        player_pick = switch_door                           # to switch

    if player_pick == prize_door:                           # If the player picked the prize door then they won!
        wins += 1                                           # So increment wins

win_percentage = wins/PLAY_TIMES

if will_switch:                                             # Print results
    print ("\nYou won the car", wins, "out of", PLAY_TIMES, "times (or about",
           format(win_percentage, ".2%"), "of the time) by switching from your initial pick.")
else:
    print("\nYou won the car", wins, "out of", PLAY_TIMES, "times (or about",
          format(win_percentage, ".2%"), "of the time) by keeping your initial pick.")
		  
input("\nPress any key to exit")