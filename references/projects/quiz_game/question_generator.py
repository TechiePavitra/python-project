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