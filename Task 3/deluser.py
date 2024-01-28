from password_util import read_password_file, write_password_file

def delete_user():
    file_path = 'passwd.txt'

    username = input("Enter username: ").strip().lower()

    password_file_data = read_password_file(file_path)

    updated_data = [line for line in password_file_data if not line.startswith(username + ":")]

    if len(updated_data) == len(password_file_data):
        print("User not found. Nothing changed.")
    else:
        write_password_file(file_path, updated_data)
        print("User Deleted.")

if __name__ == "__main__":
    delete_user()
