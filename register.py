import json
import random
import classlar1
import login


def a_register():
    print("Register Page\n")
    print("Tizimda ro'yxatdan o'tish uchun quydagi ma'lumotlarni kiriting:")
    with open("jsonlar/users.json", 'r') as file:

        data = json.load(file)
        data_usernames = [user["username"] for user in data["users"]]

    while True:
        username = input("Username: ")

        if login.check_usernames(username, data_usernames):
            print(f"Ushbu {username} nomli foydalanuvchi tizimda mavjud! Boshqa username kiriting!")
        else:
            break

    first_name = input(" >>> First Name: ")
    last_name = input(" >>> Last Name: ")
    while True:
        gmail = input("Gmail _________________@gmail.com shu ko'rinishda kiriting: ")
        data = gmail.split("@gmail")

        if len(data) == 2 and data[1].endswith(".com"):
            print("Gmail qabul qilindi.")

            break
        else:
            print("  Noto'g'ri email...!!! Qaytadan kiriting: ")
    password = input(" Password :")
    password1 = input(" Password 1 : ")
    while password != password1 and len(password1) != 5:
        print(" Parol uzunligi 5 belgidan kam bo'lasligi kerak")
        password1 = input("Password qaytadan kiriting: ")

    phone_number = input("Telefon raqam : +998 ")
    while len(phone_number) != 9 or not phone_number.isdigit():
        print("Tel nomer 9 ta raqamdan iborat bo'lishi lozim !")
        phone_number = input("Telefon raqamingizni kiriting (9 ta raqamdan iborat bo'lishi lozim): +998 ")

    generated_code = f"{random.randint(1000, 9999):04d}"
    print(f" Telefon raqamingizga yuborilgan kod: {generated_code}")

    entered_code = input("Kodni kiriting: ")

    while entered_code != generated_code:
        print("Noto'g'ri kod! Qayta urinib ko'ring.")
        entered_code = input("Kodni kiriting: ")

    if password == password1:
        register = classlar1.Register(username, password, phone_number, gmail, first_name, last_name, False, 0)
        print("\n<<< Registration was successful >>>\n")
        register.new_users()
        return login.login_check()
