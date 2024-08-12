import random


def main():
    with open('countries_list.txt') as file:
        data = file.read()

    country = random.choice(data.split('\n'))
    print(country)


if __name__ == '__main__':
    main()
