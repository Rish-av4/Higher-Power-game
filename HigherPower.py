logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
import os
import random
from data import data

os.system("cls")
print(logo)

def format_data(account):
    the_name = account["name"]
    the_description = account["description"]
    the_location = account["country"]
    return (f"{the_name}, a {the_description}, from {the_location}")

def check_answer(guess, a_followers, b_followers):
    ''' Take the user guess and follower counts and returns if statement to check if user is correct or not '''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

account_b = random.choice(data)

score = 0
game_must_go_on = True

''' Making the game more repeatable '''

while game_must_go_on:

    account_a = account_b
    account_b = random.choice(data)
    # account_b = random.choice(data)  Isko upar shift kr diya global bna dia 
    while account_a == account_b:
        account_b = random.choice(data)


    #  Format the data into printable format

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    #  Ask user for a guess

    guess = input("Who has more followers A or B ? Type 'A' or 'B' : ").lower()

    # Check if user is correct or not
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system("cls")

    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current Score is: {score}")
    else:
        game_must_go_on = False
        print(f"Sorry that's wrong!. Score is: {score}")


   

    



    
        

