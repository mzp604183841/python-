import csv

# fileName = 'sitka_weather_07-2014.csv'
# with open(fileName) as file:
#     reader = csv.reader(file)
#     header_row = next(reader)
#     print(header_row)
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)


# fileName = 'sitka_weather_07-2014.csv'
# with open(fileName) as file:
#     reader = csv.reader(file)
#     head_row = next(reader)
#
#     highs = []
#     # 拿到所有的最高温度
#     for row in reader:
#         highs.append(row[1])
#     print(highs)


fileName = 'sitka_weather_07-2014.csv'
with open(fileName) as file:
    reader = csv.reader(file)
    highs = []
    num = 1
    for row in reader:
        if num == 1:
            num += 1
            continue
        highs.append(int(row[1]))
    print(highs)