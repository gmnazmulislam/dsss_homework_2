import random

def generate_random_integer(min_val, max_val):
    """
    Generating a random integer between a given minimum and maximum value
    """
    return random.randint(min_val, max_val)

def generate_operator():
    """
    Generating an arithmetic operator: +/ - / *
    """
    return random.choice(['+', '-', '*'])

def evaluate_problem(num1, num2, operator):
    """
    Evaluate the problem based on the provided numbers and operator
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+': 
        ans = num1 + num2
    elif operator == '-': 
        ans = num1 - num2
    else:
        ans = num1 * num2
    return problem, ans

def math_quiz():
    """
    A math quiz game where users have to answer arithmetic questions.
    """
    score = 0
    total_questions = 3  # change float to integer as no of question can't be a fraction.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)  # change 5.5 to 5 as randint does not support float
        operator = generate_operator()

        problem, ans = evaluate_problem(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError as e:
            print("Invalid input")
            continue

        if user_answer == ans:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ans}.")

    print(f"\nGame over! Your score is: {score}/{total_question}")

if __name__ == "__main__":
    math_quiz()
