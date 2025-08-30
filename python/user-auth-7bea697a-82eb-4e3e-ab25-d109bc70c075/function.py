import bcrypt, jwt, datetime

SECRET_KEY = "super_secret_key"

def authenticate_user(username: str, password: str, db):
    """
    Authenticate user and return JWT token if valid.
    """
    user = db.get_user(username)
    if not user:
        raise ValueError("User not found")

    if not bcrypt.checkpw(password.encode(), user["password_hash"].encode()):
        raise ValueError("Invalid password")

    token = jwt.encode({
        "user_id": user["id"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, SECRET_KEY, algorithm="HS256")

    return token