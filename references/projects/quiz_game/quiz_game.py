# Database function
def build_question(question, options, correct_answer, points):
    """Creates a new question"""
    question = {
        "question": question,
        "options": options,
        "correct_ans": correct_answer,
        "points": points,
    }
    return question

# Added questions
questions = []
questions.append(build_question("what is the capital of australia?", ["sydney", "melbourne", "canberra", "perth"], "c", 1_000))
questions.append(build_question("what is the capital of india?", ["kolkata", "mumbai", "new delhi", "surat"], "c", 2_000))
questions.append(build_question("which planet is known as the red planet?", ["venus", "mars", "jupiter", "saturn"], "b", 3_000))
questions.append(build_question("who wrote the play 'romeo and juliet'?", ["charles dickens", "william shakespeare", "mark twain", "jane austen"], "b", 5_000))
questions.append(build_question("which country is famous for the pyramids of giza?", ["mexico", "greece", "egypt", "india"], "c", 10_000))
questions.append(build_question("what is the chemical symbol for gold?", ["ag", "gd", "go", "au"], "d", 20_000))
questions.append(build_question("how many continents are there on earth?", ["5", "6", "7", "8"], "c", 40_000))
questions.append(build_question("which animal is known as the king of the jungle?", ["tiger", "elephant", "lion", "leopard"], "c", 80_000))
questions.append(build_question("which gas do plants absorb from the atmosphere?", ["oxygen", "nitrogen", "carbon dioxide", "hydrogen"], "c", 160_000))
questions.append(build_question("who was the first person to walk on the moon?", ["yuri gagarin", "buzz aldrin", "michael collins", "neil armstrong"], "d", 500_000))    
    
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