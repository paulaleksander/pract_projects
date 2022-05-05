import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and precipitation from this file.
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rains.append(rain)
        
# Plot the precipitations.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='green', alpha=0.5)
plt.fill_between(dates, rains, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily precipitaions - 2018", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitations (mm)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('Precipitations Sitka')
