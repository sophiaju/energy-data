# from pkgutil import get_data
# from posixpath import abspath
import psycopg2
import os
import pandas as pd
import argparse
from get_data import *
from insert_tables import *

def main():
    '''
    example command used: python src/extract_and_load.py -d 01 -m 03 -y 2022
    '''

    # take arguments for date
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', required=True, help="day format '01'")
    parser.add_argument('-m', '--month', required=True, help="month format '01'")
    parser.add_argument('-y', '--year', required=True, help="year format '01'")
    args = parser.parse_args()
    day = str(args.day)
    month = str(args.month)
    year = str(args.year)

    # downloads data for all cycles of a given day over http
    file_names_list = get_data_for_day(day, month, year)

    # for each file that was just downloaded
    for file_name in file_names_list:

        abs_path = os.path.abspath(file_name)
        # print(abs_path)

        # insert that file into the database
        upload_file_to_db(abs_path, host = 'localhost', dbname = 'name', user = 'postgres', table='oac_tw')
        print(f"Inserted {file_name} into oac_tw table")


if __name__ == '__main__':
    main()
