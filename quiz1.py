questions = ("Which of the following is the correct extension of the python file? ",
             "Which of the following is used to define a block of the code in python language?",
             "Which of the following character is used to give single line comments in python?",
             "Which keyword is used for function in Python language?",)
options = (("A. .python", "B. .pl", "C. .py", "D. .p"),
           ("A. Indentation", "B. Key", "C. Brackets", "D. All of the above"),
           ("A. //", "B. #", "C. !", "D. /*"),
           ("A. Function", "B. def", "C. Fun", "D. Define"))
answers = ("C", "A", "B", "B")
guesses = []
score = 0
question_num = 0
for question in questions:
      print("-------------------------")
      print(question)

      for option in options[question_num]:
          print(option)

      guess = input("Enter (A,B,C,D):").upper()
      guesses.append(guess)
      if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
      else:
        print("INCORRECT!")
        print(f"{answers[question_num]}is the correct answer")
      question_num += 1

print("----------------------")
print("        RESULT        ")
print("----------------------")

print("answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions)*100)
print(f"Your score is: {score}%")

print("Thank you")