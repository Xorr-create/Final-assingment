from password_util import encrypt_password, read_password_file, write_password_file

def add_user():
    file_path = 'passwd.txt'

    username = input("Enter new username: ").strip().lower()
    real_name = input("Enter real name: ").strip()
    password = input("Enter password: ")

    password_file_data = read_password_file(file_path)

    for line in password_file_data:
        if line.startswith(username + ":"):
            print("Cannot add. Most likely username already exists.")
            return

    encrypted_password = encrypt_password(password)
    new_entry = f"{username}:{real_name}:{encrypted_password}"

    password_file_data.append(new_entry)
    write_password_file(file_path, password_file_data)

    print("User Created.")

if __name__ == "__main__":
    add_user()
