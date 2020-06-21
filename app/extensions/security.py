from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password, met):
    return generate_password_hash(password, method=met)