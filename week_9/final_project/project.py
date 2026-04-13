"""
CS50P Final Project: Python Proficiency Quiz
Author: Marcos [Teu Sobrenome]
Description: A command-line quiz game that tests Python knowledge 
             with questions loaded from a CSV file.
"""

import csv
import pyfiglet
import random
import sys


def main():
    """Runs the main quiz game loop, handling user flow and scoring."""
    print()
    f = pyfiglet.figlet_format("CS50P   Quiz")
    print(f)
    
    name = input("What's your name? ")
    print(f"\nWelcome, {name}, to CS50P Quiz!\n")
    
    level_input = choose_level()
    level = get_level_name(level_input)
    print()
    
    all_questions = load_questions()
    questions_to_play = filtered_questions(all_questions, level)
    
    game_questions = random.sample(questions_to_play, 10)
    score = 0
    q_number = 1
    for q in game_questions:
        print("Question ", q_number, "/10: ", q["question"], sep="")
        q_number = q_number + 1
        print("[A]",q["choice_a"])
        print("[B]",q["choice_b"])
        print("[C]",q["choice_c"])
        print("[D]",q["choice_d"])
        user_answer = input("Your answer: ")
        if check_answer(user_answer, q["answer"]):
            print("✅ Correct! +10 points\n")
            score = score + 10
        else:
            # It builds dinamically the key (ex.: choice_a) to obtain the text of the correct answer
            correct_text = q[f"choice_{q['answer'].lower()}"]
            print(f"❌ Wrong! The correct answer is [{q['answer']}] {correct_text}\n")
    
    print(f"Game Over, {name}!\n")
    print(f"Your final score is: {score} out of 100!\n")


def choose_level():
    """Prompts the user for a difficulty level and validates the input."""
    while True:
        try:
            level = int(input("Choose Level [0 - Easy] [1 - Medium] [2 - Hard] [3 - Veteran]:\n"))
            if level in [0,1,2,3]:
                return level
            else:
                continue
        except ValueError:
            print("Please enter a number (0-3).\n")


def get_level_name(level_input):
    """Converts integer level input into the corresponding string category."""
    if level_input == 0:
        level = "Easy"
    elif level_input == 1:
        level = "Medium"
    elif level_input == 2:
        level = "Hard"
    elif level_input == 3:
        level = "Veteran"
    return level


def load_questions():
    """Reads questions from the CSV file and return them as a list of dictionaries. Also handles missing file errors."""
    questions = []
    try:
        with open("questions.csv", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                questions.append(
                    {"question": row["question"],
                    "choice_a": row["choice_a"],
                    "choice_b": row["choice_b"],
                    "choice_c": row["choice_c"],
                    "choice_d": row["choice_d"],
                    "answer": row["answer"],
                    "level": row["level"]}
                    )
        return questions
    except FileNotFoundError:
        print("\nError: 'questions.csv' not found. Please make sure the file exists.")
        sys.exit(1)


def filtered_questions(all_questions, level):
    """Filters the questions list to return only those matching the selected level."""
    filtered_questions = []
    for question in all_questions:
        if question["level"] == level:
            filtered_questions.append(question)
    return filtered_questions


def check_answer(user_answer, correct_answer):
    """Validates if the user's input matches the correct answer."""
    if user_answer.strip().upper() == correct_answer:
        return True
    else:
        return False


if __name__ == "__main__":
    main()