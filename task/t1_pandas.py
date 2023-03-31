import pandas as pd


data_frame = pd.read_csv('f1.csv')

max_temperature = data_frame['Max TemperatureC']
min_temperature = data_frame['Min TemperatureC']

temperature_difference = max_temperature - min_temperature

temperature_difference_list = temperature_difference.tolist()

print(temperature_difference_list)
