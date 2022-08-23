import pandas as pd

# Read the Pbl File into a dataframe
df = pd.read_csv('pbl_table.csv',sep=',')

# Create Empty lists for all the three columns
unique_sector_id = []
lat = []
long = []

# Loop through each row in the csv file and append the lists.
for i in df.index:
    unique_sector_id.append(df["Unique Sector ID"][i])
    # Number Improved Position Entries greater than 0,
    # Take lat and long values from "Improved Position" Column
    if df[" Number Improved Position Entries"][i] > 0:
        pos_list = df[" Improved Position"][i].split(";")
        lat.append(pos_list[0].strip().replace('"',''))
        long.append(pos_list[1].strip())
    # Number Improved Position Entries Equal to 0,
    # Take lat and long values from "Raw Position" Column
    else:
        pos_list = df[" Raw Position"][i].split(";")
        # print(Lat)
        lat.append(pos_list[0].strip().replace('"',''))
        long.append(pos_list[1].strip())

#Create dataframe with the three lists and write to the csv file.
csv_data = {'Unique Sector ID' : unique_sector_id,
            'Lat' : lat,
            'Long' : long}
df = pd.DataFrame(csv_data)
df.to_csv('Final_pbl_table.csv', index=False)

