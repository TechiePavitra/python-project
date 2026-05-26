# Database
questions = [{
    "question": "what is the capital of australia?",
    "options": ["sydney", "melbourne", "canberra", "perth"],
    "correct_ans": "c",
    "points": 1_000,
},
{
    "question": "what is the capital of india?",  
    "options": ["kolkata", "mumbai", "new delhi", "surat"],  
    "correct_ans": "c",  
    "points": 2_000,   
},
{
    "question": "which planet is known as the red planet?",
    "options": ["venus", "mars", "jupiter", "saturn"],
    "correct_ans": "b",
    "points": 3_000, 
},
{
    "question": "who wrote the play 'romeo and juliet'?",
    "options": ["charles dickens", "william shakespeare", "mark twain", "jane austen"],
    "correct_ans": "b",
    "points": 5_000, 
},
{
    "question": "which country is famous for the pyramids of giza?",
    "options": ["mexico", "greece", "egypt", "india"],
    "correct_ans": "c",
    "points": 10_000, 
},
{
    "question": "what is the chemical symbol for gold?",
    "options": ["ag", "gd", "go", "au"],
    "correct_ans": "d",
    "points": 20_000, 
},
{
    "question": "how many continents are there on earth?",
    "options": ["5", "6", "7", "8"],
    "correct_ans": "c",
    "points": 40_000, 
},
{
    "question": "which animal is known as the king of the jungle?",
    "options": ["tiger", "elephant", "lion", "leopard"],
    "correct_ans": "c",
    "points": 80_000, 
},
{
    "question": "which gas do plants absorb from the atmosphere?",
    "options": ["oxygen", "nitrogen", "carbon dioxide", "Hydrogen"],
    "correct_ans": "c",
    "points": 160_000, 
},
{
    "question": "who was the first person to walk on the moon?",
    "options": ["yuri gagarin", "buzz aldrin", "michael collins", "neil armstrong"],
    "correct_ans": "d",
    "points": 500_000, 
},
]

# Score Tracking
total_score = 0
index = 0

# Option Labels
labels = ["A", "B", "C", "D"]
    
# While loop
while index < len(questions):

    question = questions[index]
    print(f"\n{question['question'].title()}")

    # Print options
    i = 0
    while i < len(question["options"]):
        print(f"{labels[i]}) {question['options'][i].title()}")
        i += 1

    # User input
    choice = input("Enter your choice here: ")

    # Check answer
    if choice.lower() == question["correct_ans"]:
        print("Correct Answer!")
        total_score += question["points"]
        print(f"Earned Points: {total_score}$")

    else:
        print("Wrong Answer!")
        print(f"Game Over! You earned {total_score}$.")
        break

    index += 1

# If player completes all questions
if index == len(questions):
    print("\nCongratulations! You completed the quiz.")
    print(f"Total Points: {total_score}$")