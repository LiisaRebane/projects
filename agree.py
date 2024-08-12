while True:
    c = input("Do you agree? (y/n): ").capitalize()

    if c == 'Y':
        print("Agreed.")
        break
    elif c == 'N':
        print("Not agreed.")

