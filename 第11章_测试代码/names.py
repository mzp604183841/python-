from name_function import get_formated_name

print('Enter q at any time to quit')
while True:
    first = input('\n Please give me a fisrt name: ')
    if first == 'q':
        break
    last = input('\n Please give me a last name')
    if last == 'q':
        break

    formatted_name = get_formated_name(first, last)
    print('\nNeatly formatted name :' + formatted_name + '.')
