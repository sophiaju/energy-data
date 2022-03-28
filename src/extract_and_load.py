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
    example command used: python src/extract_and_load.py
    '''

    print("This script will use a postgreSQL database \n")
    print("Enter the database host: ")
    host = input()
    print("Enter the database name: ")
    dbname = input()
    print("Enter the database user: ")
    user = input()
    # print("Enter the table name: ")
    # table = input()

    # print(host, dbname, user, table)

    # interactive loop
    txt = ''
    while not txt == 'stop':

        print("Enter the day (DD): ")
        day = input()
        print("Enter the month (MM): ")
        month = input()
        print("Enter the year (YYYY): ")
        year = input()
    

        # downloads data for all cycles of a given day over http
        try: 
            file_names_list = get_data_for_day(day, month, year)

        except Exception as err: 
            print(f"Could not retrieve CSV due to error: {err}")
            
        else:
            # if there was something to download
            if file_names_list != []:

                print("Insert these CSVs into the database? (Y/N)")
                
                insert = input()

                if insert == 'Y':

                    # for each file that was just downloaded
                    for file_name in file_names_list:

                        abs_path = os.path.abspath(file_name)
                        # print(abs_path)

                        # insert that file into the database
                        upload_file_to_db(abs_path, host, dbname, user, table='oac_tw')
                        print(f"Inserted {file_name} into oac_tw table")
                else:
                    print("Did not insert CSVs")

            # if all files have been downloaded, there is nothing to insert 
            else:
                print("Nothing to insert")


        print("Enter 'stop' if you want to stop, or press 'enter' to repeat for another day: ")
        txt = input()


if __name__ == '__main__':
    main()
