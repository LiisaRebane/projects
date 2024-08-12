"""convert kg into g and vice versa"""

import time


# get user input and perform conversion
def converter():
    while True:
        print("(1) From kg to g\n(2) From g to kg\n(3) to QUIT")
        user_input = input("> ")
        try:
            if user_input == '1':
                kg = int(input("> kg: "))
                print(f">> {kg} kg = {kg_to_g(kg)}g")
            elif user_input == '2':
                g = int(input("> g: "))
                print(f">> {g} g = {g_to_kg(g)}kg")
        except ValueError:
            print("Must be a number")
        time.sleep(0.5)
        if user_input == '3':
            break


# convert g to kg
def g_to_kg(int_):
    return int_ / 1000


# convert kg to g
def kg_to_g(int_):
    return int_ * 1000


if __name__ == '__main__':
    converter()
