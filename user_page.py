import json
import Asosiy
import classlar1
import random
import login


def user_info(username, password):
    print(classlar1.User.get_info(username, password))
    back = input(" ====>>>> 0. Back\n\t >>>>>> ")
    if back == "0":
        return profile(username, password)
    else:
        print(" Nolni bosing xato buyruq kiritdiz!!!\n ")
        print("=======================================================")
        return user_info(username, password)


def change_first_name(username, password):
    print(" Userning ismini o'zgartirish 🔄")
    new_first_name = input(" Enter the New First Name:")
    print(classlar1.User.change("first_name", username, password, new_first_name))
    return user_change_info(username, password)


def change_last_name(username, password):
    print(" Userning familasini o'zgartirish 🔄")
    new_last_name = input(" New Last Name:")
    print(classlar1.User.change("last_name", username, password, new_last_name))
    return user_change_info(username, password)


def change_username(username, password):
    print(" Userning Usernameni  o'zgartirish 🔄")
    with open("jsonlar/users.json", 'r') as f:
        data = json.load(f)
        data_usernames = [users["username"] for users in data["users"]]
    while True:
        new_username = input("Enter the new Username name: ")
        if login.check_usernames(new_username, data_usernames):
            print(f"Ushbu {username} nomli foydalanuvchi tizimda mavjud! Boshqa username kiriting!")
        else:
            break

    print(classlar1.User.change("username", username, password, new_username))
    return user_change_info(username, password)


def change_pasword(username, password):
    print(" Userning Passwordni o'zgartirish 🔄")
    new_password = input(" New Password :")
    print(classlar1.User.change("password", username, password, new_password))
    return user_change_info(username, password)


def change_gmail(username, password):
    print(" Userning Gamilni o'zgartirish 🔄")
    while True:
        new_gmail = input("Email (example@gmail.com) yoki (example@email.com) shu ko'rinishda kiriting: ")
        data = new_gmail.split("@gmail")

        if len(data) == 2 and data[1].endswith(".com"):
            print("Gmail qabul qilindi.")

            break
        else:
            print("  Noto'g'ri email...!!! Qaytadan kiriting: ")
    print(classlar1.User.change("gmail", username, password, new_gmail))
    return user_change_info(username, password)


def change_phone_number(username, password):
    print(" Userning Telefon nomerini o'zgartirish 🔄")
    new_phone_number = input(" New Telephone Number :")
    print(classlar1.User.change("phone_number", username, password, new_phone_number))
    return user_change_info(username, password)


def change_full_change(username, password):
    print(" Userning hamma ma'lumotni o'zgartirish 🔄")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    with open("jsonlar/users.json", 'r') as file:
        data = json.load(file)
        data_usernames = [user_1["username"] for user_1 in data["users"]]
    while True:
        new_username = input("Enter the new username: ")
        if login.check_usernames(new_username, data_usernames):
            print(f"Ushbu {new_username} nomli foydalanuvchi tizimda mavjud! Boshqa username kiriting!")
        else:
            break

    while True:
        new_gmail = input("Email (example@email.com) shu ko'rinishda kiriting: ")
        data = new_gmail.split("@email")
        if len(data) == 2 and data[1].endswith(".com"):
            print("Email qabul qilindi.")
            break
        else:
            print("Noto'g'ri email. Qaytadan kiriting.")
    phone_number = input("Telefon raqamingiz kiriting: +998 ")
    while len(phone_number) != 9 or not phone_number.isdigit():
        print("Tel nomer 9 ta raqamdan iborat bo'lishi lozim !")
        phone_number = input("Telfon nomerini quydagi raqamlar keyin kodi bilan kiritish lozim  ")

    generated_code = f"{random.randint(1000, 9999):04d}"
    print(f" Telefon raqamingizga yuborilgan kod: {generated_code}")

    entered_code = input("Kodni kiriting: ")

    while entered_code != generated_code:
        print("Noto'g'ri kod! Qayta urinib ko'ring.")
        entered_code = input("Kodni kiriting: ")

    password = input("Password: ")
    password1 = input("Enter the password again: ")

    while len(password) != 5 or password != password1:
        print("Parol uzunligi 5 belgidan kam bo'lasligi kerak")
        password1 = input("Enter the password again: ")

    new_data = {
        "first_name": first_name,
        "last_name": last_name,
        "username": new_username,
        "password": password,
        "gmail": new_gmail,

    }
    print(classlar1.User.change("new_data", username, password, new_data))
    return user_change_info(username, password)


def user_change_info(username, password):
    about = input("""
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                QAYSI MA'LUMOTLARNI O'ZGARTIRMOQCHISIZ:
            
                        1. First Name
                        2. Last Name
                        3. Username
                        4. Password 
                        5. Gmail
                        6. Phone Number
                        7. Full Change
                        0. Back
                        
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️   
        
                         ⏩⏩ """)

    if about == "1":
        return change_first_name(username, password)

    elif about == "2":
        return change_last_name(username, password)

    elif about == "3":
        return change_username(username, password)

    elif about == "4":
        return change_pasword(username, password)

    elif about == "5":
        return change_gmail(username, password)

    elif about == "6":
        return change_phone_number(username, password)

    elif about == "7":
        return change_full_change(username, password)

    elif about == "0":
        return profile(username, password)
    else:
        print("Xato buyruq kiritdingiz !!!")
        return user_change_info(username, password)


def user_balance(username, password):
    title = input("""
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                 ====>>>>  Balance  <<<<===== 
                    ====>>>> 1. Balance Info
                    ====>>>> 2. Add balance
                    ====>>>> 0. Back
     ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                            ====⏩⏩⏩⏩ """)

    if title == "1":
        print(classlar1.User.balance(username, password))
        return user_balance(username, password)

    elif title == "2":
        new_money = float(input(" ===>>> Qancha mablag' kiritmoqchisiz? <<<<===== "))
        while new_money < 0:
            print("Mablag'ni to'g'ri kiriting (0 dan katta va son bo'lishi kerak)!")
            new_money = float(input("Qancha mablag' kiritmoqchisiz? >>> "))
        current_balance = classlar1.User.get_billing(username, password)
        new_balance = current_balance + new_money

        print(classlar1.User.change("billing", username, password, new_balance))
        print(f"====>>>> Hozirgi hisobingiz: {new_balance} So'm <<<<====")
        return user_balance(username, password)

    elif title == "0":
        return profile(username, password)

    else:
        print(" Xato buyruq kiritdingiz !!! ")
        return user_balance(username, password)


def profile(username, password):
    service = input("""
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                 ====>>>> User Profile  <<<<===== 
                    ====>>>> 1. Info
                    ====>>>> 2. Change Info
                    ====>>>> 3. Balance
                    ====>>>> 0. Back
     ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                            ====⏩⏩⏩⏩ """)

    if service == "1":
        return user_info(username, password)

    elif service == "2":
        return user_change_info(username, password)

    elif service == "3":
        return user_balance(username, password)

    elif service == "0":
        return user(username, password)

    else:
        print("Error!")
        return profile(username, password)


def user(username, password):
    print("This is user page")

    header = input("""
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                 ========> User Page <========
                 
                    ====> 1. Profile <====
                    ====> 2. Courses <====
                    ====> 3. Speciality <====
                    ====> 0. Log Out <====
                    
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
            ====⏩⏩⏩⏩ """)

    if header == "1":
        return profile(username, password)

    if header == "2":
        data = classlar1.Course.get_all_course()
        for i in data:
            print(f"""
                       ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                       ==============>>>> Course Ma'lumotlari <<<<==============
                                       name : {i["name"]}
                                       gradution : {i["gradution"]}
                                       description : {i["description"]}
                                       buying_users : {i["buying_users"]}
                                       price : {i["price"]}
                                       mentor : {i["mentor"]}
                                       hours : {i["hours"]}
                                       reyting : {i["reyting"]}
                                       active_users : {i["active_users"]}
                                       lenguege : {i["lenguege"]}
                                       create_date : {i["create_date"]}
                       ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                   """)
            print("===============================================================\n")
        return user(username, password)

    elif header == "3":
        data = classlar1.Speciality.get_all_speciality()
        for i in data:
            print(f"""
                ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                                name: {i["name"]}
                                description: {i["description"]}
                                gradution: {i["gradution"]}
                                create_date: {i["create_date"]}
                ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
            """)
            print("__________________________________________\n")
        return user(username, password)

    elif header == "0":
        return Asosiy.main()

    else:
        print("Error!\n Bunday service mavjud emas")
        return user(username, password)


data =  [Bek, Nur , Ali]
for i in data:
    print(i)
