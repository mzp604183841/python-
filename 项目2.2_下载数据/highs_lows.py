from matplotlib import pyplot as plt
import csv
from datetime import datetime

fileName = 'sitka_weather_2014.csv'
with open(fileName) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    isHead = True
    for row in reader:
        if isHead:
            isHead = False
            continue
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        highs.append(int(row[1]))
        lows.append(int(row[3]))

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, lows, c='red', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)

plt.title('Daily high&low temperatures, 2014', fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperatures', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
