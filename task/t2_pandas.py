import pandas as pd

data_frame = pd.read_csv('f1.csv')

max_temperature = data_frame['Max TemperatureC']
min_temperature = data_frame['Min TemperatureC']

temperature_average = (max_temperature - min_temperature)/2

average_temperature_list = temperature_average.tolist()

print(average_temperature_list)
