# energy-data
TEC Energy Dev Candidate Project

Energy data project to extract CSVs from https://twtransfer.energytransfer.com/ipost/TW/capacity/operationally-available and inserts into a PostgreSQL database

## Installation
This was created using Python3


Requirements are in `requirements.txt`

Use pip to install required packages:
```bash
pip install -r requirements.txt
```

## Usage
This program assumes that the PostgreSQL database already exists (can have any name)

The main program is executed by running `extract_and_load.py` from the energy-data directory and creates a table named "oac_tw"

example command: 
```bash 
python src/extract_and_load.py
```

The table "oac_tw" can also be created and dropped by running `createtbl.sql` and `droptbl.sql` respectively

example command:
```bash
psql -U user -d dbname -f C:/absolute_path/src/createtbl.sql
```

## Current limitations and edge cases
- does not create database, assumes database is already created
- table name is hardcoded
- assumes that if data is downloaded (file exists), then it is already in the database
    - if data is deleted but the data is not dropped from the table, then it will try to insert the same day’s data again
- 01_03_2022 is considered different day as 1_3_2022 but both work for downloading data, so it will try to insert the same data twice
- saves empty values as empty string “”
- assumes all cycles available for every day