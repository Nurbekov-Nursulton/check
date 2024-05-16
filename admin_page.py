import Asosiy
import classlar1
import json
import login
import random


def user_info(username, password):
    print(classlar1.User.get_info(username, password))
    back = input(" ====>>>> 0. Back\n\t >>>>>> ")
    if back == "0":
        return admin_profile(username, password)
    else:
        print(" Nolni bosing xato buyruq kiritdiz!!!\n ")
        print("=======================================================")
        return user_info(username, password)


def change_first_name(username, password):
    print(" Userning ismini o'zgartirish 🔄")
    new_first_name = input(" Enter the New First Name:")
    print(classlar1.User.change("first_name", username, password, new_first_name))
    return admin_change_info(username, password)


def change_last_name(username, password):
    print(" Userning familasini o'zgartirish 🔄")
    new_last_name = input(" New Last Name:")
    print(classlar1.User.change("last_name", username, password, new_last_name))
    return admin_change_info(username, password)


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
    return admin_change_info(username, password)


def change_pasword(username, password):
    print(" Userning Passwordni o'zgartirish 🔄")
    new_password = input(" New Password :")
    print(classlar1.User.change("password", username, password, new_password))
    return admin_change_info(username, password)


def change_gmail(username, password):
    print(" Userning Gamilni o'zgartirish 🔄")
    while True:
        new_gmail = input("Email (example@gmail.com) shu ko'rinishda kiriting: ")
        data = new_gmail.split("@gmail")

        if len(data) == 2 and data[1].endswith(".com"):
            print("Gmail qabul qilindi.")

            break
        else:
            print("  Noto'g'ri gmail...!!! Qaytadan kiriting: ")
    print(classlar1.User.change("gmail", username, password, new_gmail))
    return admin_change_info(username, password)


def change_phone_number(username, password):
    print(" Userning Telefon nomerini o'zgartirish 🔄")
    new_phone_number = input(" New Telephone Number :")
    print(classlar1.User.change("phone_number", username, password, new_phone_number))
    return admin_change_info(username, password)


def change_full_change(username, password):
    print("Hamma ma'lumotni o'zgartirish 🔄")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    with open("jsonlar/users.json", 'r') as file:
        data = json.load(file)
        data_usernames = [user["username"] for user in data["users"]]
    while True:
        new_username = input("Usernameningizni kiriting : ")
        if login.check_usernames(new_username, data_usernames):
            print(f" {new_username} bu Admin_user bor! Boshqa kiriting!")
        else:
            break

    while True:
        new_gmail = input("Gmail ____________@gmail.com oxiri kiriting: ")
        data = new_gmail.split("@gmail")
        if len(data) == 2 and data[1].endswith(".com"):
            print("Gmail tasdiqlandi.")
            break
        else:
            print("Noto'g'ri Gmail. Qaytadan kiriting.")
    phone_number = input("Telefon raqamingiz = +998 ")
    while len(phone_number) != 9 or not phone_number.isdigit():
        print("Telefon raqamingiz kiriting: +998! ")
        phone_number = input("Telefon raqamingiz =  +998 ")

    generated_code = f"{random.randint(1000, 9999):04d}"
    print(f"Kod: {generated_code}")

    entered_code = input("Kodni kiriting: ")

    while entered_code != generated_code:
        print("Noto'g'ri kod! Qayta urinib ko'ring.")
        entered_code = input("Kodni kiriting: ")

    password = input("Password: ")
    password1 = input("Enter the password again: ")

    while len(password) != 5 or password != password1:
        print("Parol uzunligi 5 belgidan kam bo'lasligi kerak")
        password1 = input("Password qaytadan kiriting: ")

    new_data = {
        "first_name": first_name,
        "last_name": last_name,
        "username": new_username,
        "password": password,
        "gmail": new_gmail,

    }
    print(classlar1.User.change("new_data", username, password, new_data))
    return admin_change_info(username, password)


def admin_change_info(username, password):
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
        return admin_profile(username, password)
    else:
        print("Xato buyruq kiritdingiz !!!")
        return admin_change_info(username, password)


def admin_profile(username, password):
    admin_service = input("""
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                 ====>>>>  Admin Profile  <<<<===== 
                    ====>>>> 1. Info
                    ====>>>> 2. Change Info
                    ====>>>> 3. Salary
                    ====>>>> 0. Back
     ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                            ====⏩⏩⏩⏩ """)

    if admin_service == "1":
        return user_info(username, password)

    elif admin_service == "2":
        return admin_change_info(username, password)

    elif admin_service == "3":
        print(classlar1.User.admin_salary(username, password))
        return admin_profile(username, password)

    elif admin_service == "0":
        return admin(username, password)

    else:
        print("Bunday buyruq mavjud esmas !")
        return admin_profile(username, password)


def admin(username, password):
    print("This is Admin page")

    admin_header = input("""
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                 ========>>> Admin page <<<========     
                    ====> 1. Profile <====
                    ====> 2. Course <====
                    ====> 3. User <====
                    ====> 4. Speciality <====
                    ====> 5. Modul <====
                    ====> 0. Log Out <====
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
            ====⏩⏩⏩⏩ """)

    if admin_header == "1":
        return admin_profile(username, password)

    if admin_header == "2":
        data = classlar1.Course.get_all_course()
        for i in data:
            print(f"""
                       ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                       =============>>>> Admin Courses ma'lumotlari : <<<<==============
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
        return admin(username, password)

    elif admin_header == "3":
        data = classlar1.User.get_info(username, password)
        for i in data:
            print(f"""
                        ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                                        username: {i["username"]}
                                        password: {i["password"]}
                                        first_name: {i["first_name"]}
                                        last_name: {i["last_name"]}
                                        gmail: {i["gmail"]}
                                        billing: {i["billing"]}
                                        phone_number: {i["phone_number"]}
                                        create_date : {i["create_date"]}
                        ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                    """)
            print("__________________________________________\n")

        return admin(username, password)



    elif admin_header == "4":
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
        return admin(username, password)

    elif admin_header == "5":
        data = classlar1.Modul.get_all_modul()
        for i in data:
            print(f"""
                   ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                                   name: {i["name"]}
                                   price: {i["price"]}
                                   lessons_count: {i["lessons_count"]}
                                   description: {i["description"]}
                                   active_users: {i["active_users"]}
                                   create_date: {i["create_date"]}
                   ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
               """)
            print("__________________________________________\n")
        return admin(username, password)


    elif admin_header == "0":
        return Asosiy.main()

    else:
        print("Error!\n Bunday service mavjud emas")
        return admin(username, password)
