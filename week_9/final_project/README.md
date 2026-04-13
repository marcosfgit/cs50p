# Python Proficiency Quiz
#### Video Demo: [https://youtu.be/47YCjOexUPo](https://youtu.be/47YCjOexUPo)
#### Description:

This project is a command-line interface (CLI) quiz game designed to test Python knowledge. It was developed as the final project for Harvard's **CS50's Introduction to Programming with Python**.

The application loads a set of questions from a CSV file, allowing for easy updates and a large pool of data. Players can choose between four difficulty levels, and the game randomly selects 10 questions for each session.

## Features
- **Dynamic Question Loading:** All questions are stored in `questions.csv`, making the game data-driven.
- **Difficulty Levels:** Users can select from Easy, Medium, Hard, and Veteran levels.
- **Randomized Gameplay:** Every round is unique thanks to the `random.sample` logic.
- **Detailed Feedback:** When a question is missed, the system displays both the correct letter and the full answer text to enhance learning.

## File Structure
- `project.py`: The main script containing the game logic and core functions.
- `test_project.py`: A suite of Pytest functions to ensure the reliability of the logic.
- `requirements.txt`: Lists the external dependencies (`pyfiglet`) required to run the game.
- `questions.csv`: A structured database containing questions, choices, answers, and difficulty levels.

## Implementation Details
The project follows modular programming principles:
- `choose_level`: Handles input validation using while and try-except for numbers 0-3.
- `get_level_name`: Converts numerical input into a string-based category.
- `load_questions`: Handles file I/O using the `csv.DictReader` class.
- `filtered_questions`: Implements list comprehension to isolate questions by difficulty.
- `check_answer`: Validates user input against the correct key, ensuring case-insensitivity.

## Installation
To run this project, you need to install the dependencies:
```bash
pip install -r requirements.txt
```

To start the game:
```bash
python project.py
```

Testing
To run the automated tests and verify the functions:
```bash
pytest test_project.py
```