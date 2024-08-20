# quiz.py

from answers import answers

def ask_question(prompt, expected_type):
    """Helper function to ask questions and parse inputs."""
    while True:
        try:
            response = input(prompt)
            # If the expected type is a tuple or list, evaluate it
            if expected_type in [list, tuple]:
                return expected_type(eval(response))
            # Otherwise, directly cast
            return expected_type(response)
        except (ValueError, SyntaxError):
            print(f"Invalid input. Please enter a {expected_type.__name__}.")

def main():
    user_answers = []

    # Q1
    print("Q1: Determine the evaluation of each expression")
    user_answers.append([
        ask_question("v = 12 % 5: ", int),
        ask_question("w = 2 * 3 + 2: ", int),
        ask_question("x = 'a' < 'b': ", bool),
        ask_question("y = 'a' < 'a': ", bool),
        ask_question("z = 1 == True: ", bool),
    ])

    # Q2
    print("\nQ2: Determine the evaluation of each expression")
    user_answers.append([
        ask_question("a = 6 ** 2: ", int),
        ask_question("b = (5 % 2) ** 2: ", int),
        ask_question("c = str(234) + '5': ", str),
        ask_question("d = a // b: ", int),
    ])

    # Q3
    print("\nQ3: Determine the value of variable q3 at each line")
    user_answers.append([
        ask_question("q3 = 10: ", int),
        ask_question("q3 += 5: ", int),
        ask_question("q3 -= 10: ", int),
        ask_question("q3 *= 2: ", int),
        ask_question("q3 = str(q3): ", str),
        ask_question("q3 += '1': ", str),
    ])

    # Q4
    print("\nQ4: Determine the output of the program")
    user_answers.append([
        ask_question("x = 1, while loop outputs: ", int),
    ])

    # Q5
    print("\nQ5: Determine the output of the program")
    user_answers.append([
        ask_question("Output of the program: ", str),
    ])

    # Q6
    print("\nQ6: Determine the output of the program")
    user_answers.append([
        ask_question("Output 1: ", str),
        ask_question("Output 2: ", str),
    ])

    # Q7
    print("\nQ7: Determine the output of the program")
    user_answers.append([
        ask_question("Value of x: ", int),
    ])

    # Q8
    print("\nQ8: Determine the output of the program")
    user_answers.append([
        ask_question("d['tim']: ", int),
        ask_question("d[6]: ", str),
    ])

    # Q9
    print("\nQ9: Determine the output of the program")
    user_answers.append([
        ask_question("Final answer of ans: ", bool),
    ])

    # Q10
    print("\nQ10: Determine which of the following expressions is the same as q10")
    user_answers.append([
        ask_question("Choose the correct option (a, b, c, d): ", str),
    ])

    # Q11
    print("\nQ11: Determine the output of the program")
    user_answers.append([
        ask_question("lst[::2]: ", list),
        ask_question("lst[::-1]: ", list),
        ask_question("lst[1:2]: ", list),
        ask_question("lst[2]: ", int),
        ask_question("lst[-1]: ", int),
    ])

    # Q12
    print("\nQ12: Determine the output of the program")
    user_answers.append([
        ask_question("lst[::2]: ", tuple),
        ask_question("lst[::-1]: ", tuple),
        ask_question("lst[1:2]: ", tuple),
        ask_question("lst[2]: ", int),
        ask_question("lst[-1]: ", int),
    ])

    # Q13
    print("\nQ13: Does the following code produce an error, if so why?")
    user_answers.append([
        ask_question("Error explanation: ", str),
    ])

    # Q14
    print("\nQ14: Does the following code produce an error, if so why?")
    user_answers.append([
        ask_question("Error explanation: ", str),
    ])

    # Q15
    print("\nQ15: Does the following code produce an error, if so why?")
    user_answers.append([
        ask_question("Error explanation: ", str),
    ])

    # Q16
    print("\nQ16: Determine the output of the following program")
    user_answers.append([
        ask_question("Output 1: ", list),
        ask_question("Output 2: ", list),
    ])

    # Q17
    print("\nQ17: Determine the output of the following program")
    user_answers.append([
        ask_question("Count of 'a': ", int),
    ])

    # Q18
    print("\nQ18: Determine the output of the following program")
    user_answers.append([
        ask_question("Joined string: ", str),
    ])

    # Q19
    print("\nQ19: Determine the output of the following program")
    user_answers.append([
        ask_question("Output: ", str),
    ])

    # Q20
    print("\nQ20: Determine the output of the following program")
    user_answers.append([
        ask_question("Output list: ", list),
    ])

    # Q21
    print("\nQ21: Determine the output of the following program")
    user_answers.append([
        ask_question("x is y: ", bool),
        ask_question("id(x) == id(y): ", bool),
        ask_question("New y, x is y: ", bool),
        ask_question("New id check, id(x) == id(y): ", bool),
        ask_question("Final x: ", list),
        ask_question("Final y: ", list),
    ])

    # Q22
    print("\nQ22: Determine the output of the following program")
    user_answers.append([
        ask_question("Output 1: ", int),
        ask_question("Output 2: ", int),
        ask_question("Output 3: ", int),
        ask_question("Output 4: ", int),
        ask_question("Output 5: ", int),
    ])

    # Q23
    print("\nQ23: Determine the output of the following program")
    user_answers.append([
        ask_question("Total evens: ", int),
        ask_question("Last small number: ", int),
    ])

    # Q24
    print("\nQ24: Determine the output of the following program")
    user_answers.append([
        ask_question("Number 1: ", int),
        ask_question("Number 2: ", int),
        ask_question("Number 3: ", int),
        ask_question("Number 4: ", int),
        ask_question("Number 5: ", int),
        ask_question("Number 6: ", int),
    ])

    # Q25
    print("\nQ25: Determine the output of the following program")
    user_answers.append([
        ask_question("Line 1: ", str),
        ask_question("Line 2: ", str),
        ask_question("Line 3: ", str),
        ask_question("Line 4: ", str),
    ])

    # Q26
    print("\nQ26: Determine the output of the following program")
    user_answers.append([
        ask_question("Line 1: ", list),
        ask_question("Line 2: ", list),
        ask_question("Line 3: ", list),
        ask_question("Line 4: ", list),
        ask_question("Line 5: ", list),
        ask_question("Line 6: ", list),
    ])

    # Q27
    print("\nQ27: Determine the output of the following program")
    user_answers.append([
        ask_question("Index 1: ", int),
        ask_question("Index 2: ", int),
        ask_question("Index 3: ", int),
        ask_question("Index 4: ", int),
        ask_question("Index 5: ", int),
        ask_question("Index 6: ", int),
    ])

    # Q28
    print("\nQ28: Determine the output of the following program")
    user_answers.append([
        ask_question("Swapped list: ", list),
    ])

    # Q29
    print("\nQ29: Determine the output of the following program")
    user_answers.append([
        ask_question("2D list row 1: ", list),
        ask_question("2D list row 2: ", list),
        ask_question("2D list row 3: ", list),
        ask_question("2D list row 4: ", list),
        ask_question("2D list row 5: ", list),
        ask_question("2D list row 6: ", list),
        ask_question("2D list row 7: ", list),
        ask_question("2D list row 8: ", list),
        ask_question("2D list row 9: ", list),
        ask_question("2D list row 10: ", list),
    ])

    # Q30
    print("\nQ30: Determine the output of the following program")
    user_answers.append([
        ask_question("Row 1: ", list),
        ask_question("Row 2: ", list),
        ask_question("Row 3: ", list),
        ask_question("Row 4: ", list),
        ask_question("Row 5: ", list),
    ])

    # Compare answers and calculate scores
    correct_count = 0
    incorrect_indices = []

    for i, (correct, user) in enumerate(zip(answers, user_answers)):
        if correct == user:
            correct_count += 1
        else:
            incorrect_indices.append(i + 1)

    # Print results
    total_questions = len(answers)
    print(f"\nYour final score is {correct_count}/{total_questions}.")
    print(f"You got {correct_count} questions right and {total_questions - correct_count} questions wrong.")

    if incorrect_indices:
        print("You got the following questions wrong:")
        for index in incorrect_indices:
            print(f"Question {index}")

if __name__ == "__main__":
    main()
