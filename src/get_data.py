import pandas as pd
import os
import argparse


def get_data_for_day(day, month, year):
    '''
    downloads data for all cycles of a given day over http
    day: string like "01"
    month: string like "03"
    year: string like "2022"
    '''

    # directory name for that day
    dir_name = os.path.join('data', f'{day}_{month}_{year}')
    
    file_names_list = []

    # make a directory for that day
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    # pairs cycle names with matching number for url
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

        # add date and cycle attributes
        data['date'] = f'{year}-{month}-{day}'
        data['cycle'] = cycle

        #print(data[48:50])

        file_name = os.path.join(dir_name,f'{cycle}.csv')


        # check if the file already exists
        if os.path.exists(file_name):
            print("Data has already been downloaded here: ", file_name)

        # if not, make new file
        else:
            data.to_csv(file_name, sep='\t', index=False)
            print("Downloaded: ", file_name)
            file_names_list.append(file_name)

        
    return file_names_list

def main():
    month = '03'

    day = '01'

    year = '2022'

    get_data_for_day(day, month, year)

if __name__ == '__main__':
    main()
