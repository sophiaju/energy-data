import psycopg2

# connect to the database
conn = psycopg2.connect("host=localhost dbname=name user=postgres")

# create cursor object to execute commands
cur = conn.cursor()

# i already created the tables
# later, combine the creating and inserting

# make this an argument?
with open("C:/Users/sophi/Documents/TEC/energy-data/data/test_data.csv", "r") as file:
    
    # skip header row
    next(file)
    cur.copy_from(file, table='test_energy_data', null='')

# commit to database
conn.commit()

# close communication with database
cur.close()
conn.close()
