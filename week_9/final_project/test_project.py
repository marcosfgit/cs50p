from project import get_level_name, check_answer, filtered_questions


def test_get_level_name():
    """Verify that level IDs are correctly converted to their string names."""
    assert get_level_name(0) == "Easy"
    assert get_level_name(1) == "Medium"
    assert get_level_name(2) == "Hard"
    assert get_level_name(3) == "Veteran"


def test_check_answer():
    """Verify answer validation logic, including case-insensitivity and whitespace."""
    assert check_answer("a", "A") is True
    assert check_answer("A", "A") is True
    assert check_answer("  b  ", "B") is True
    assert check_answer("a", "B") is False
    assert check_answer("b", "C") is False
    assert check_answer("", "A") is False


def test_filtered_questions():
    """Verify that questions are correctly filtered by their difficulty level."""
    mock_data = [
        {"question": "Question 1?", "level": "Easy"},
        {"question": "Question 2?", "level": "Hard"},
        {"question": "Question 3?", "level": "Easy"}
    ]

    easy = filtered_questions(mock_data, "Easy")
    assert len(easy) == 2
    hard = filtered_questions(mock_data, "Hard")
    assert len(hard) == 1
    empty = filtered_questions(mock_data, "Veteran")
    assert len(empty) == 0
