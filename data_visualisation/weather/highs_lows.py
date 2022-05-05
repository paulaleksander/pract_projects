import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    date = 'DATE'
    tmax = 'TMAX'
    tmin = 'TMIN'
    name = 'NAME'
    i_name = header_row.index(name)
    i_date = header_row.index(date)
    i_tmax = header_row.index(tmax)
    i_tmin = header_row.index(tmin)
    
           
    # Get dates, high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[i_date], '%Y-%m-%d')
        try:
            high = int(row[i_tmax])
            low = int(row[i_tmin])
            name = str(row[i_name])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = f"Daily high and low temperatures - 2018\n{name}"
plt.title("", fontsize=20)
plt.xlabel(title,fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

