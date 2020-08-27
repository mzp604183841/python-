import json

number = [1, 2, 4, 5, 1, 5, 6]
fileName = 'number.json'
with open(fileName, 'w') as f_obj:
    json.dump(number, f_obj)
