fileName = 'pi_digits.txt'

with open(fileName) as file_object:
    lines = file_object.readlines()

piString = ''
for line in lines:
    piString += line.strip()

print(piString)
print(len(piString))