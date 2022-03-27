import pandas as pd
import os

data = pd.read_csv('https://twtransfer.energytransfer.com/ipost/capacity/operationally-available?f=csv&extension=csv&asset=TW&gasDay=01%2F24%2F2022&cycle=1&searchType=NOM&searchString=&locType=ALL&locZone=ALL', dtype={'DC':'Int64'})

print(data[48:50]['DC'])

data.to_csv(os.path.join('data','test_data.csv'), sep='\t', index=False)