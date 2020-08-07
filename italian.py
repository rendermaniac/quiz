import random
import webbrowser

correctly_answered = 0

words = {   "uno" : "one",
            "due" : "two",
            "tre" : "three",
            "quattro" : "four",
            "cinque" : "five",
            "sei" : "six" }

questions = list(words.keys())
random.shuffle(questions)
number_questions = len(questions)

for number, word in enumerate(questions):
    print(f"Question {number+1} of {number_questions}")
    print("="*15)
    print(f"What is the meaning of the word {word}? \n")
    correct = words[word]
    choices = set([])
    choices.add(correct)
    while len(choices) < 3:
        x = random.choice(list(words.values()))
        if x != correct:
            choices.add(x)

    choices = list(choices)
    random.shuffle(choices)

    pick = ["a", "b", "c"]
    for i, c in enumerate(choices):
        print(f"{pick[i]}: {c}")
    answer_string = input("\nEnter your answer (a,b or c): ")

    while answer_string not in pick:
        answer_string = int(input(f"\nInvalid choice {answer}.\n Enter your answer (a, b or c): "))

    answer = pick.index(answer_string)

    if choices[answer] == correct:
        print("\nCORRECT!")
        correctly_answered += 1
    else:
        print(f"\nSorry the answer was {correct}")
    print("\n")

print(f"Quiz complete! You got {correctly_answered} words correct out of {number_questions}")

if correctly_answered == number_questions:
    webbrowser.open_new("http://www.youtube.com/watch?v=LDU_Txk06tM&t=1m14s")
else:
    webbrowser.open_new("https://www.youtube.com/watch?v=KolfEhV-KiA&t=0m19s")



