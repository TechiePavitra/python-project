def build_question(question, options, correct_answer, points):
    """Creates a new question"""
    question = {
        "question": question,
        "options": options,
        "correct_ans": correct_answer,
        "points": points,
    }
    return question

# Creates a New Question in Dictionary,
# You need to store this dictionary in a list,
# This function requires Question, all the options, correct answer,
# and lastly points given to player.