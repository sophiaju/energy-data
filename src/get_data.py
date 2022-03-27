import pandas as pd
import os
import argparse

# must be run from the energy_data folder

#data = pd.read_csv('https://twtransfer.energytransfer.com/ipost/capacity/operationally-available?f=csv&extension=csv&asset=TW&gasDay=01%2F24%2F2022&cycle=1&searchType=NOM&searchString=&locType=ALL&locZone=ALL', dtype={'DC':'Int64'})

month = '03'

day = '01'

year = '2022'

# directory name for that day
dir_name = os.path.join('data', f'{day}_{month}_{year}')

# make a directory for that day
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

cycle_dict = {
    'timely':0,
    'evening':1,
    'intra1':3,
    'intra2':4,
    'intra3':7,
    'final':5}

# get all cycles for each day
for cycle, num in cycle_dict.items():
    
    # download data into a dataframe
    data = pd.read_csv(f'https://twtransfer.energytransfer.com/ipost/capacity/operationally-available?f=csv&extension=csv&asset=TW&gasDay={month}%2F{day}%2F{year}&cycle={num}&searchType=NOM&searchString=&locType=ALL&locZone=ALL', dtype={'DC':'Int64'})

    # print(data[48:50]['DC'])

    
    file_name = os.path.join(dir_name,f'{cycle}.csv')

    # check if the file already exists
    if os.path.exists(file_name):
        print("Data has already been downloaded here: ", file_name)

    else:
        data.to_csv(file_name, sep='\t', index=False)
        print("Downloaded: ", file_name)

