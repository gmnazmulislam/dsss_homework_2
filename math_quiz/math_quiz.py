import random

def generate_random_integer(min_value, max_value):
    """
    Generating a random integer between a given minimum and maximum value
    """
    return random.randint(min_value, max_value)

def generate_operator():
    """
    Generating a random arithmetic operator: +/ - / *
    """
    return random.choice(['+', '-', '*'])

def evaluate_expression(number1, number2, operator):
    """
    Evaluate the expression based on provided numbers and operator
    """
    expression = f"{number1} {operator} {number2}"
    if operator == '+': 
        answer = number1 + number2
    elif operator == '-': 
        answer = number1 - number2
    else:
        answer = number1 * number2
    return expression, answer

def math_quiz():
    """
    A math quiz game where users have to answer arithmetic questions.
    """
    score = 0
    total_questions = 3  # change float to integer as no of question can't be fraction.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)  # change 5.5 to 5 as randint does not support float
        operator = generate_operator()

        problem, answer = evaluate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError as e:
            print("Invalid input")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_question}")

if __name__ == "__main__":
    math_quiz()
