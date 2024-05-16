import json
from datetime import datetime


class Login:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def info(self):
        return f"{self.username}{self.password}"

    def get_username(self):
        return f"{self.username}"

    def get_password(self):
        return f"{self.password}"

    def __str__(self):
        return f"{self.username} {self.password}"


class User(Login):
    id = 1

    def __init__(self, username, password, phone_number, gmail, first_name: str, last_name: str, status: bool,
                 billing: float):
        Login.__init__(self, username, password)
        self.id = User.id
        self.first_name = first_name
        self.last_name = last_name
        self.gmail = gmail
        self.status = status
        self.billing = billing
        self.phone_number = phone_number
        self.create_date = f"{datetime.now().date()}"
        User.id += 1

    @staticmethod
    def get_billing(username, password):
        with open("jsonlar/users.json", "r") as file:
            data = json.load(file)
            for i in data["users"]:
                if i["username"] == username and i["password"] == password:
                    return i["billing"]

    @staticmethod
    def balance(username, password):
        with open("jsonlar/users.json", "r") as file:
            data = json.load(file)
            for i in data["users"]:
                if i["username"] == username and i["password"] == password:
                    money = f"""
                    =====================================================
                       ====>>>> Sizning balansingiz <<<<====

                       ====>>>>  Balance: {i["billing"]} So'm <<<<====
                    =====================================================
                        """
            return money

    @staticmethod
    def admin_salary(username, password):
        with open("jsonlar/users.json", "r") as file:
            data = json.load(file)
            for i in data["users"]:
                if i["username"] == username and i["password"] == password:
                    admin_money = f"""
                        =====================================================
                           ====>>>> Sizning balansingiz <<<<====

                           ====>>>>  Salary: {i["salary"]} So'm <<<<====
                        =====================================================
                            """
            return admin_money

    @staticmethod
    def get_info(username, password):
        with open("jsonlar/users.json", 'r') as file:
            data = json.load(file)

            for i in data["users"]:
                if i["username"] == username and i["password"] == password:
                    if i["status"] == 1:
                        admin_user = f"""
                            ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                                        ====> First Name : {i["first_name"]}
                                        ====> Last Name : {i["last_name"]}
                                        ====> Username : {i["username"]}
                                        ====> Password : {i["password"]}
                                        ====> Gmail : {i["gmail"]}
                                        ====> Phone Number : {i["phone_number"]}
                                        ====> Salary: {i["salary"]}
                             ️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                            """
                        return admin_user

                    else:
                        user = f"""
                        ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                                    ====> First Name : {i["first_name"]}
                                    ====> Last Name : {i["last_name"]}
                                    ====> Username : {i["username"]}
                                    ====> Password : {i["password"]}
                                    ====> Gmail : {i["gmail"]}
                                    ====> Phone Number : {i["phone_number"]}
                                    ====> Billing: {i["billing"]}
                        ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                        """
                    return user

    @staticmethod
    def change(argument, username, password, new_data):
        if argument != "full_name":
            with open("jsonlar/users.json", "r") as file:
                data = json.load(file)
                users = data["users"]
                for i in users:
                    if i["username"] == username and i["password"] == password:
                        user = i
                users.remove(user)
                user[argument] = new_data
                users.append(user)
                data["users"] = users

            with open("jsonlar/users.json", "w") as f:
                json.dump(data, f, indent=6)
            return "Bajarildi..............!"
        else:
            with open("jsonlar/users.json", "r") as file:
                data = json.load(file)
                users = data["users"]
                for i in users:
                    if i["username"] == username and i["password"] == password:
                        user = i
                users.remove(user)
                keys = new_data.keys()
                for i in keys:
                    user[i] = new_data[i]
                users.append(user)
                data["users"] = users

            with open("jsonlar/users.json", "w") as f:
                json.dump(data, f, indent=6)
            return "Bajarildi..............!"

    @staticmethod
    def profile_full_info(username, password):
        with open("jsonlar/users.json", 'r') as file:
            data = json.load(file)
            for i in data["users"]:
                if i["username"] == username and i["password"] == password:
                    user = f"""
                      "Username": {i["username"]}
                      "Password":{i["password"]}
g                      "First_name": {i["first_name"]}
                      "Last_name": {i["last_name"]}
                      "Billing": {i["billing"]}
                  """
            return user

    def __str__(self):
        return f"{self.id} {self.username} {self.password} {self.first_name} {self.last_name} {self.gmail} {self.status} {self.create_date} "


class Register(User):
    def __init__(self, username, password, phone_number, gmail, first_name, last_name, status, billing):
        User.__init__(self, username, password, phone_number, gmail, first_name, last_name, status, billing)
        self.create_date = f"{datetime.now().date()}"

    def save_data_user(self):
        with open("jsonlar/users.json", "r") as file:
            data = json.load(file)
            new_user = {
                "username": self.username,
                "password": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "gmail": self.gmail,
                "status": self.status,
                "billing": self.billing,
                "phone_number": self.phone_number,
                "create_date": self.create_date
            }
            users = data["users"]
            users.append(new_user)
            data["users"] = users

        with open("jsonlar/users.json", "w") as f:
            json.dump(data, f, indent=6)


class Student(User):
    def __init__(self, username, password, phone_number, first_name, last_name, gmail, status: 0, courses: list):
        User.__init__(self, username, password, phone_number, first_name, last_name, gmail, status, billing=0)
        self.courses = courses


class Speciality:

    def __init__(self, name: str, gradution: int, description: str):
        self.name = name
        self.gradution = gradution
        self.description = description
        self.create_date = f"{datetime.now()}"

    @staticmethod
    def get_all_speciality():
        with open("jsonlar/speciality.json", "r") as file:
            data = json.load(file)
            return data["speciality"]


class Course:
    def __init__(self, name: str, gradution: int, description: str, buying_users: float, price: float, hours: float,
                 reyting: int, active_users: int, language: str):
        self.name = name
        self.gradution = gradution
        self.description = description
        self.buying_users = buying_users
        self.price = price
        self.hours = hours
        self.reyting = reyting
        self.active_users = active_users
        self.language = language
        self.create_date = datetime.now().date()

    @staticmethod
    def get_all_course():
        with open("jsonlar/courses.json", "r") as file:
            data = json.load(file)
            return data["courses"]


class Modul:

    def __init__(self, name, price: float, lessons_count: int, description: str, active_users: int):
        self.name = name
        self.price = price
        self.lessons_count = lessons_count
        self.description = description
        self.active_users = active_users
        self.create_date = datetime.now()
        

    @staticmethod
    def get_all_modul():
        with open("jsonlar/modul.json", "r") as file:
            data = json.load(file)
            return data["moduls"]


class Lesson:
    def __init__(self, name, homework: None, deadline, status):
        self.name = name
        self.homework = homework
        self.deadline = deadline
        self.status = status
        self.date = datetime.now().date()
