from password_util import encrypt_password, read_password_file, write_password_file

def change_password():
    file_path = 'passwd.txt'

    username = input("User: ").strip().lower()
    current_password = input("Current Password: ")
    new_password = input("New Password: ")
    confirm_password = input("Confirm: ")

    password_file_data = read_password_file(file_path)

    for i, line in enumerate(password_file_data):
        if line.startswith(username + ":"):
            _, _, existing_password = line.split(":")
            if existing_password == encrypt_password(current_password) and new_password == confirm_password:
                password_file_data[i] = f"{username}:{line.split(':')[1]}:{encrypt_password(new_password)}"
                write_password_file(file_path, password_file_data)
                print("Password changed.")
            else:
                print("Invalid current password or passwords do not match. No change made.")
            return

    print("User not found. No change made.")

if __name__ == "__main__":
    change_password()
