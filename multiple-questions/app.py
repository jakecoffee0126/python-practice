from Question import Questions

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What color are Bnanas?\n(a) Teal\n(b) Yellow\n(c) Pink\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# create the objects
questions = [
    Questions(question_prompts[0], 'a'),
    Questions(question_prompts[1], 'b'),
    Questions(question_prompts[2], 'b')
]


def run_test(questions):  # questions here is a list of questions
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))


run_test(questions)
