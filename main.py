from src.calculator import get_iinfo
from src.data_fetcher import get_latest_version

print("Game Version = " + get_latest_version())

def calculation():
    get_iinfo()
    q_decision = int(input("1: try again\n2: quit\n"))
    if q_decision == 1:
        get_iinfo()
    elif q_decision ==2:
        quit()

while True:
    try:
        a = int(input("\n1:calculate\n2:quit\n"))
        if a == 1:
            calculation()
        elif a == 2:
            quit()
        else:
            print("Invalid Number")
    except ValueError:
        print("Invalid Input")