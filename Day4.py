def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")


def user_exists(username, password):
    try:
        with open("users.txt", "r") as f:
            for line in f:
                stored_username, stored_password = line.strip().split(",")
                if stored_username == username and stored_password == password:
                    return True
    except FileNotFoundError:
        return False
    return False


def login():
    print("--- Login Section ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user_exists(username, password):
        print(f"✅ Welcome back, {username}!")
    else:
        print("❌ Wrong username or password!")


def create_account():
    print("--- Account Creation ---")
    username = input("Choose username: ")
    password = input("Choose password: ")
    save_user(username, password)
    print(f"✅ Account created successfully for {username}!")


print('-----------------')
print("--- Welcome to the Central Bank ---")
print("1 --- Logging into the user account ---")
print("2 --- Creating a user account ---")

green = input("Enter your selection: ")

if green == "1":
    login()
elif green == "2":
    create_account()
else:
    print("--- Anonymous input option ---")