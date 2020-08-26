alien_dict = {'color': 'green', 'point': 5}
print(alien_dict)
print(alien_dict['color'])

human_dict = {'name': 'mzp', 'age': 12}
print(human_dict)


for key, value in human_dict.items() :
    print('key : ' + str(key) + 'value : ' + str(value))
