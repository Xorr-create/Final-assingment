from password_util import encrypt_password, read_password_file

def login():
    file_path = 'passwd.txt'

    username = input("User: ").strip().lower()
    password = input("Password: ")

    password_file_data = read_password_file(file_path)

    for line in password_file_data:
        if line.startswith(username + ":"):
            _, _, stored_password = line.split(":")
            if stored_password == encrypt_password(password):
                print("Access granted.")
            else:
                print("Access denied.")
            return

    print("User not found. Access denied.")

if __name__ == "__main__":
    login()
