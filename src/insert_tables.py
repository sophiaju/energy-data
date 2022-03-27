import psycopg2
import os

def create_table(cur, conn, dbname, table):
    # check if table already exists
    cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='oac_tw')")
    if bool(cur.fetchone()[0]):
        print(f'{table} table exists, moving on')
    else:
        print(f'Creating {table} table now')
        
        cur.execute("""
        CREATE TABLE oac_tw 
        (loc INTEGER, 
        loc_zn VARCHAR(20), 
        loc_name VARCHAR(50), 
        loc_purp_desc VARCHAR(2), 
        loc_qti VARCHAR(3), 
        flow_ind VARCHAR(1), 
        DC INTEGER, 
        OPC INTEGER, 
        TSQ INTEGER, 
        OAC INTEGER, 
        IT VARCHAR(1), 
        auth_over_ind VARCHAR(1), 
        nom_cap VARCHAR(1), 
        all_qty_avail VARCHAR(1), 
        qty_reason VARCHAR(30), 
        day DATE, 
        cycle VARCHAR(10), 
        PRIMARY KEY(loc, loc_purp_desc, day, cycle));
        """)

        print("Table created")

        #conn.commit()

def insert_csv_to_table(cur, file_name, table):
    # make this an argument?
    with open(file_name, "r") as file:
        
        # skip header row
        next(file)
        cur.copy_from(file, table=table, null='')

def upload_file_to_db(file_name, host = 'localhost', dbname = 'name', user = 'postgres', table='oac_tw'): 
    '''
    loads data from csv into the postgresql database
    file_name: absolute path to csv with data
    host: name of database host
    dbname: name of database
    user: name of user
    '''

    # connect to the database
    conn = psycopg2.connect(f"host={host} dbname={dbname} user={user}")

    # create cursor object to execute commands
    cur = conn.cursor()

    # create table if needed
    create_table(cur, conn, dbname, table)

    # upload csv at file_name to desired table in database
    insert_csv_to_table(cur, file_name, table)

    print("Inserted CSV to table")

    # commit to database
    conn.commit()

    # close communication with database
    cur.close()
    conn.close()

def main():

    file_name = "C:/Users/sophi/Documents/TEC/energy-data/data/01_03_2022/evening.csv"

    table = 'oac_tw'

    upload_file_to_db(file_name, host = 'localhost', dbname = 'name', user = 'postgres', table = 'oac_tw')


if __name__ == '__main__':
    main()