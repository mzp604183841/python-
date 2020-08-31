import csv
from matplotlib import pyplot as plt
from datetime import datetime

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


# fileName = 'sitka_weather_07-2014.csv'
# with open(fileName) as file:
#     reader = csv.reader(file)
#     highs, dates = [], []
#     isHead = True
#     for row in reader:
#         if isHead:
#             isHead = False
#             continue
#         current_date = datetime.strptime(row[0], '%Y-%m-%d')
#         dates.append(current_date)
#         highs.append(int(row[1]))
#
#     print(highs)
#
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red')
# plt.title('Daily high temperatures, July 2014', fontsize=20)
# plt.xlabel('', fontsize=14)
# fig.autofmt_xdate()
# plt.ylabel('Temperatures', fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

