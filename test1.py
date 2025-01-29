def get_greeting_text(user_name: str) -> str:
    correct_username = user_name.strip() if user_name else user_name
    if correct_username:
        correct_username = user_name.strip()
        return f"Привет, {correct_username}!"
    return 'Привет!'
