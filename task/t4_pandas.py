import pandas as pd
from datetime import datetime

data_frame = pd.read_csv('f2.csv')

thunderstorm_data = data_frame[data_frame[' Events'] == 'Thunderstorm']

thunderstorm_days = [datetime.strptime(date, "%Y-%m-%d").strftime("%A")
                     for date in thunderstorm_data['PKT']]

print(thunderstorm_days)
