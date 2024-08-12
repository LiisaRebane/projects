def main():
    print("""
==================================
            CALCULATOR       
==================================
   write the values of x and y
          """)
    while True:
        try:
            x = int(input("value of x: "))
            break
        except ValueError:
            print("Must be a number!")

    while True:
        try:
            y = int(input("value of y: "))
            break
        except ValueError:
            print("Must be a number!")

    z = add(x, y)
    print(f"\n{x} + {y} = {z}\n")


def add(a, b):
    return a + b


main()