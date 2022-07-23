usernamePasswordPairs = {
    "mike": "danieljack123",
    "jack": "superhero21",
    "daisy": "mariosucks69"
}

username = input ("what is your username: ")
password = input ("what is your password: ")

def check_username(username):
    if usernamePasswordPairs.get(username, "None") != "None":
        return True
    else:
        return False

def check_password(username, password):
    if usernamePasswordPairs.get(username) == password:
        return True
    else:
        return False

is_username_correct = check_username(username)
is_pasword_correct = check_password(username, password)

if is_username_correct:
    if is_pasword_correct:
        print("Login Successful")
    else:
        print("Password incorrect")
else:
    print("Username incorrect")
