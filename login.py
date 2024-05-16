import json
import admin_page
import user_page
import register


def check_usernames(username, data_user_names):
    return username in data_user_names


def login_check():
    print("Login Page")
    username = input("Username: ")
    password = input("Password: ")
    with open("jsonlar/users.json", 'r') as file:
        data = json.load(file)
        for i in data["users"]:
            if i["username"] == username and i["password"] == password:
                if i["status"] == 1:
                    return admin_page.admin(username, password)
                else:
                    return user_page.user(username, password)
        print("""  
                   ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                   >>>>>>>>>>>>>>      Xato kiritdingiz    <<<<<<<<<<<<<<
                           Username  yoki Password xato kiritildingiz !
                   ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                   ⏩⏩
        """)

        print("===============================================================================\n")

        register_1 = input("""
        ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                Login yoki Parolingizni unutdingizmi....?  
                Qaytadan ro'yahatdan o'tishni istaysizmi ???
        ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                                    1. Ha
                                    2. Yo'q
        ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
        ⏩⏩
        """)
        if register == "1":
            return register_1
        else:
            return login_check()
