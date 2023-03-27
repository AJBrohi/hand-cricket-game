import random

def toss():
    toss_list = ['head', 'tails']
    
    toss_choice = input("Please type Head or Tails - ").lower()

    # toss_choice = "head"

    toss_result = random.choice(toss_list)
    
    if toss_choice == toss_result:
        return True
    else:
        return False

print("Instructions\n")

total_balls=int(input("How many balls you want to play? - "))
total_wickets=int(input("How many wickets you want to play? - "))

# total_balls = 6
# total_wickets = 1


play_first = ['bat', 'ball']

print("Toss")
toss_win = toss()
who_win = ""


if toss_win:
    who_win = "You"
    print("You win the toss! Now choose what you want to play first - ")
    play_choice = input("Please type Bat or Ball - ").lower()
    # play_choice = "bat"
else:
    who_win="User"
    print("You loss the toss! Now cpu will choose what it wants to play first.")
    play_choice = random.choice(play_first)
    
print(f"{who_win} chose to play {play_choice} first.")