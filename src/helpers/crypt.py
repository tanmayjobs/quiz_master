import bcrypt


def hash_password(password: str) -> str:
    password_bytes = password.encode()
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password_bytes, salt)

    return password_hash


def check_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode(), hashed_password)
