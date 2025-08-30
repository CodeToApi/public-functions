import re

def validate_user_input(data: dict):
    """
    Validate user registration data
    """
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data.get("email", "")):
        raise ValueError("Invalid email")

    if len(data.get("password", "")) < 8:
        raise ValueError("Password too short")

    data["username"] = data["username"].strip().lower()
    return data