import pytest

from src.test1 import get_greeting_text

'''def test_get_greeting_text():
    # Arrange & Act
    text = get_greeting_text("Иван")

    # Assert

    assert text == 'Привет, Иван!'

def test_get_greeting_text_none_user__default_text():
    # Arrange & Act
    text = get_greeting_text(None)

    # Assert

    assert text == 'Привет!'

def test_get_greeting_text_blank_user__default_text():
    # Arrange & Act
    text = get_greeting_text('')

    # Assert

    assert text == 'Привет!'

def test_get_greeting_text_spaces_user__default_text():
    # Arrange & Act
    text = get_greeting_text('   Иван')

    # Assert

    assert text == 'Привет, Иван!'

def test_get_greeting_text_only_spaces_user__default_text():
    # Arrange & Act
    text = get_greeting_text('   ')

    # Assert

    assert text == 'Привет!'
'''

@pytest.mark.parametrize(
    'user_name, expected_text',
    [
        ('Иван', 'Привет, Иван!'),
        (None, 'Привет!'),
        ('', 'Привет!'),
        ('   ', 'Привет!'),
        (' Иван  ', 'Привет, Иван!'),

    ]
)

def test_get_greeting_text(user_name, expected_text):
    #Arrange & Act
    text = get_greeting_text(user_name)

    #Assert
    assert text == expected_text