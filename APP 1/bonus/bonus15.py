import json

with open('APP 1/bonus/questions.json', 'r') as file:
    content = file.read()


data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        i = index +1
        print(i,"-",alternative)
    user_choice = int(input("enter your answer: "))
    question['user_choice'] = user_choice
    if question['user_choice'] == question["correct_answer"]:
        score = score +1

for index, question in enumerate(data):
    if question['user_choice'] == question['correct_answer']:
        result = 'correct'
    else:
        result = 'incorrect'
    message = f"{index+1} {result} - your answer: {question['user_choice']}, " \
              f"corect answer: {question['correct_answer']}"
    print(message)

print('total score:', score)