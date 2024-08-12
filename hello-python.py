names = []

while True:
    name = input("Write your name: ").capitalize()
    names.append(name)

    if name.isalpha() and len(name) > 1:
        print(f"Hello, {name}!")
        break
    else:
        print("Hello, world!")


print(names)

