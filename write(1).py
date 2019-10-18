import json

number = input("What's your favorite number? ")

with open('num.json', 'w') as f:
    json.dump(number, f)
