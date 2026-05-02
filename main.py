from src.calculator import get_iinfo
from src.data_fetcher import get_latest_version
from src.config import config

print("Game Version = " + get_latest_version())
print("Current Language = " + config.lang)

def set_lang():
    lang_choice = int(input("Choose your language\n1: English 2: Korean\n: "))
    if lang_choice == 1:
        config.lang = "en_US"
    elif lang_choice == 2:
        config.lang = "ko_KR"
    else:
        print("Invalid Choice")

while True:
    try:
        a = int(input("\n1: calculate\n2: change language\n3: quit\n"))
        if a == 1:
            while True:
                get_iinfo()
                try:
                    user_decision = int(input("1: try again\n2: change language\n3: main menu\n4: quit\n"))
                    if user_decision == 1:
                        continue
                    elif user_decision == 2:
                        set_lang()
                    elif user_decision == 3:
                        break        # back to main menu
                    elif user_decision == 4:
                        quit()
                    else:
                        print("Invalid Number")
                except ValueError:
                    print("Invalid Input")
        elif a == 2:
            set_lang()
        elif a == 3:
            quit()
        else:
            print("Invalid Number")
    except ValueError:
        print("Invalid Input")