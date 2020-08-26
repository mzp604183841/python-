name = ['mzp', '12', 'cc', '33']
for item in name :
    print(item.title() + 'lalalalalala')


print(range(1, 6))

for value in range(1, 6):
    print(value)


for i in range(10):
    for j in range(0,i):
        print("-", end=' ')

    print("")

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 计算10的阶乘
mul = 1
for i in range(1, 11):
    mul = mul * i
    print('现在的乘积是：', mul)

print(sum(range(1, 11)))

