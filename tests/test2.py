import json

with open("questions.json", "r") as file:
    content = file.read()
correct_answer = 0
wrong_answer = 0
data = json.loads(content)
for question in data:
    print(question['question_text'])
    for index, answers in enumerate(question['answers']):
        print(int(index) + 1, "-", answers)
    answer = input("Choose your answer: ")
    if int(answer) == question['correct_answer']:
        correct_answer = correct_answer + 1
    else:
        wrong_answer = wrong_answer + 1
    print("Wrong answers: ", str(wrong_answer), "/", len(data))
    print("Correct answers: ", str(correct_answer), "/", len(data))
