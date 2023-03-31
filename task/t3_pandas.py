import pandas as pd


data_frame = pd.read_csv('f2.csv')

dates_and_events = data_frame[data_frame[' Events']
                    .isin(['Snow', 'Rain', 'Rain-Snow'])]['PKT']

dates_and_events_list = dates_and_events.tolist()

print(dates_and_events_list)
