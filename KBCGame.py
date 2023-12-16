questions = [
  [
    "Which type of Programming does Python support?", "Object-oriented progrmming", "Structured programming", 
    "Functional programming","All mentioned above", 4
  ],
  [
    "Which of the following is the correct extension of the Python file?", ".Python", ".p", ".py", ".p", 3
  ],
  [
    "Which of the following character is used to give single-line comments in Python?", "//", "#", "/*","!", 2
  ],
  [
    "Which of the following is the truncation division operator in Python?", "//", "*", "/",
    "%",  1
  ],
  [
    " Which of the following functions is a built-in function in python?", "factorial()", "seed()", "sqrt()",
    "print()", 4
  ],
  [
    "Which of the following is not a core data type in Python programming?", "Tuples", "Lists", "Class","Dictionary", 3
  ],
  [
    " What arithmetic operators cannot be used with strings in Python?", "+", "-", "*", "None of above", 2
  ],
  [
    "Which of the following statements is used to create an empty set in Python?", "set()","()", "[]", "{}", 1
  ],
  [
    "To add a new element to a list we use which Python command?", "list1.addEnd(5)", "list1.addLast(5)", "list1.add(5)",
    "list1.append(5)", 4
  ],
  [
    "Which of the following is a Python tuple?", "{1 2 3}", "[1 2 3]", "(1 2 3)","{}", 3
  ],
  [
    "How is a code block indicated in Python?", "Bracket", "Indentation", "key", "None of Above", 2
  ],
  [
    "Which of the following types of loops are not supported in Python?", "Do While", "For", "While","None of Above", 1
  ],
  [
    "What keyword is used in Python to raise exceptions?", "except", "goto", "try","raise", 4
  ],
  [
    "Which of the following blocks will always be executed whether an exception is encountered or not in a program?", 
    "Try", "Catch", "Finally","None", 3
  ],
  [
    "In which language is Python written?", "C++", "C", "Java","None of Above", 2
  ],
  [
    "Which of the following statements are used in Exception Handling in Python?", "Try", "Finally", "Except","All of above", 4
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
      print("CONGRATES!!!Your the winner of this game.")
      break
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")