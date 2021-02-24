import json
import random

def main():
    with open('animals.json', 'r') as f:
        animals = json.load(f)

    print(animals['animal'][random.randint(0,19)])

if __name__ == "__main__":
    main()
