import csv
import matplotlib.pyplot as plt
import datetime as dt
import statistics

def get_monthly_av(month, daily_weather):
    """Returns the average rain, max and min temperatures for the specified month.

    Parameters:
    month: specified month in the format mmm e.g. Jan.
    daily_weather: list containing a dictionary for each day.
    """
    # create a list that only contains the daily weather for the specified month
    month_daily_weather = [day for day in daily_weather if day['month'] == month]

    rain = []
    maxt = []
    mint = []
    for day in month_daily_weather:
        rain.append(float(day['rain']))
        maxt.append(float(day['maxt']))
        mint.append(float(day['mint']))
    
    #rain = round(sum(rain)/len(rain), 2)
    avg_rain = round(statistics.mean(rain), 2)
    avg_maxt = round(statistics.mean(maxt), 2)
    avg_mint = round(statistics.mean(mint), 2)

    averages = {'month': month, 'avg_rain': avg_rain, 'avg_maxt': avg_maxt, 'avg_mint': avg_mint}
    return averages

def main():
    """Runs the main code."""
    try:
        # open csv and save data in a list
        with open('dly2237\dly2237.csv', mode='r') as fbs:
            file_reader = csv.DictReader(fbs)
            daily_weather = list(file_reader)

        # add a field containing the month as a string
        for day in daily_weather:
            day['month'] = dt.date.strftime(
                dt.datetime.strptime(day['date'],'%d-%b-%y')
                ,'%b')
        
        # compute averages for each month
        months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        averages = []
        for month in months:
            averages.append(get_monthly_av(month, daily_weather))

        # write data to a csv
        with open('monthly_averages.csv', mode='w', newline='') as fbs:
            field_names = ['month', 'avg_rain', 'avg_maxt', 'avg_mint']
            file_writer = csv.DictWriter(fbs, fieldnames=field_names)
            file_writer.writeheader()
            for average in averages:
                file_writer.writerow(average)

        # read data from the csv just created
        months = []
        rain = []
        max_temps = []
        min_temps = []
        with open('monthly_averages.csv', mode='r') as fbs:
            file_reader = csv.DictReader(fbs)
            for row in file_reader:
                months.append(row['month'])
                rain.append(row['avg_rain'])
                max_temps.append(row['avg_maxt'])
                min_temps.append(row['avg_mint'])
        
        # create the first plot for rainfall
        plt.subplot(1, 2, 1)
        plt.plot(months, rain, '*-b')
        plt.title('Rain')
        plt.ylabel('Rainfall (mm)')

         # create the second plot for max and min temperatures
        plt.subplot(1, 2, 2)
        plt.plot(months, max_temps, '*-r')
        plt.plot(months, min_temps, '*-c')
        plt.title('Temp Min/Max')
        plt.ylabel('Degrees Centigrade')

        # create a title for the two plots
        plt.suptitle('Monthly Weather in 2020')

        # display the plots
        plt.show()

    except FileNotFoundError:
        print(f'The file {csv_file} could not be found.')

if __name__ == "__main__":
    # Code in here will only execute when the file is run directly    
    main()