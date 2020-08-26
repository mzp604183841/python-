bicycles = ['a', 'b', 'c', 'd']
print(bicycles)

print(bicycles[1])
bicycles.append('e')
print(bicycles)

bicycles.insert(1, 'bb')
print(bicycles)

del bicycles[1]
print(bicycles)

bicycles.pop(1)
print(bicycles)

bicycles.pop()
print(bicycles)

bicycles.remove('f')