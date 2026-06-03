import random

score = 0
attempts = 0

while attempts < 10:
    # Bot 
    selectors = ['stone', 'paper', 'scissors']
    bot_choice = random.choice(selectors)
    
    # Prompt
    prompt = "\nEnter your choice"
    prompt += "\nEnter Stone, Paper, or Scissors:  "
    user_choice = input(prompt)

    if user_choice.lower() == bot_choice:
        print(f"The computer selected {bot_choice.title()}, and you selected {user_choice.title()}. It's a tie!")
    else:
        
        # Lost
        if user_choice.lower() == 'paper' and bot_choice == 'scissors': 
            print(f"The computer selected {bot_choice.title()}. Unfortunately, you lost!")
            break
        elif user_choice.lower() == 'scissors' and bot_choice == 'stone':
            print(f"The computer selected {bot_choice.title()}. Unfortunately, you lost!")
            break
        elif user_choice.lower() == 'stone' and bot_choice == 'paper':
            print(f"The computer selected {bot_choice.title()}. Unfortunately, you lost!")
            break
    
        # Won 
        elif user_choice.lower() == 'scissors' and bot_choice == 'paper':
            print(f"The computer selected {bot_choice.title()}. Congratulations, you won!")
            score += 1000
        elif user_choice.lower() == 'paper' and bot_choice == 'stone':
            print(f"The computer selected {bot_choice.title()}. Congratulations, you won!")
            score += 1000
        elif user_choice.lower() == 'stone' and bot_choice == 'scissors':
            print(f"The computer selected {bot_choice.title()}. Congratulations, you won!")
            score += 1000
    
    attempts += 1

print(f"Your total score is: ${score}")