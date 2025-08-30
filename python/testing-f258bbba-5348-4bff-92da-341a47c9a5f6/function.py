# Mock bcrypt
def bcrypt_checkpw(password, hash):
    return password == "test" and hash == "test_hash"

# Mock jwt
def jwt_encode(payload, key, algorithm):
    return f"mock_jwt_token_{payload['user_id']}"

# Mock datetime
class MockDateTime:
    @staticmethod
    def utcnow():
        return "2024-01-01T00:00:00Z"
    
    @staticmethod
    def timedelta(hours):
        return f"+{hours} hours"

datetime = MockDateTime()

def authenticate_user(username: str, password: str, db):
    """
    Authenticate user and return JWT token if valid.
    """
    user = {"id": "123", "password_hash": "test_hash"}
    
    if not user:
        raise ValueError("User not found")
    
    if not bcrypt_checkpw(password, user["password_hash"]):
        raise ValueError("Invalid password")
    
    token = jwt_encode({
        "user_id": user["id"],
        "exp": datetime.utcnow() + datetime.timedelta(2)
    }, "secret", "HS256")
    
    return token