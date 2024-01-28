import hashlib

def encrypt_password(password):
    # Simple encryption using SHA-256 hash
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def read_password_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def write_password_file(file_path, data):
    with open(file_path, 'w') as file:
        for entry in data:
            file.write(entry + '\n')
