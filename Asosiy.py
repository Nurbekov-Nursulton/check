import login
import register


# def main_page (username, password):
#     print(" ===> Hello welcome ✅ <==== ")

def main():
    enter = input("""
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
                        ====> 1️⃣ .Login <====
                        ====> 2️⃣.Register <====
    ⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️
    
       ⏩⏩ """)
    if enter == "1":
        return login.login_check()

    if enter == "2":
        return register.a_register()
    else:
        print(
            "                  ❌❌  Xato raqamni kiritdingiz  !!!!   \n \t                    1️⃣  yoki 2️⃣  bosing   \n  ")
        print("============================================================================\n")
        return main()


if __name__ == "__main__":
    main()
