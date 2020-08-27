# fileName = 'writing.txt'
#
# with open(fileName, 'w') as file_object:
#     file_object.write('I Love you ~!')


fileName = 'writing.txt'
with open(fileName, 'a') as file_object:
    file_object.write("\nDo you love me ?")
