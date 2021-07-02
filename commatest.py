import csv
import pandas as pd

# csv = pd.read_csv('eg.csv')


# df = pd.DataFrame(columns = ['name', 'area', 'country_code2', 'country_code3']
# ,data = ['Afghanistan', 652090, 'AF', 'AFG'])

df = pd.DataFrame(
                data=(4,4['name', 'area', 'country','code']),
                columns =["a", "b", "c", "d"])
print(df)

# with open('eg.csv', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerow(data)