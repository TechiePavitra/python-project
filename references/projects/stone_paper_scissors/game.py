import random

score = 0
attempts = 0
flag = True

while attempts < 10 and flag:
    # Bot 
    selectors = ['stone', 'paper', 'scissors']
    bot_choice = random.choice(selectors)
    
    # Prompt
    prompt = "\nEnter your choice"
    prompt += "\nEnter Stone, Paper, or Scissors:  "
    user_choice = input(prompt)
    user_choice = user_choice.lower()

    if user_choice.lower() == bot_choice:
        print(f"The computer selected {bot_choice.title()}, and you selected {user_choice.title()}. It's a tie!")
    else:
        winning_rules = {
            "scissors": "paper",
            "paper": "stone",
            "stone": "scissors",
        }

        try:
            if bot_choice == winning_rules[user_choice]:
                print(f"The computer selected {bot_choice.title()}. Congratulations, you won!")
                score += 1000
            else:
                print(f"The computer selected {bot_choice.title()}. Unfortunately, you lost!")
                flag = False
        except:
            print("Please Enter a Valid choice!")  
    attempts += 1

print(f"Your total score is: ${score}")