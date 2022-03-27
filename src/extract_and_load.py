# from pkgutil import get_data
# from posixpath import abspath
import psycopg2
import os
import pandas as pd
import argparse
from get_data import *
from insert_tables import *

def main():

    # take arguments for date
    month = '03'

    day = '02'

    year = '2022'

    # downloads data for all cycles of a given day over http
    file_names_list = get_data_for_day(day, month, year)

    # for each file that was just downloaded
    for file_name in file_names_list:

        abs_path = os.path.abspath(file_name)
        print(abs_path)

        # insert that file into the database
        upload_file_to_db(abs_path, host = 'localhost', dbname = 'name', user = 'postgres', table='oac_tw')



if __name__ == '__main__':
    main()
