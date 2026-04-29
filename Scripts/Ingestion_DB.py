# -------------------------------
# Importing Libraries
# -------------------------------

import pandas as pd 
import os
import sqlalchemy
from sqlalchemy import create_engine
import warnings
warnings.filterwarnings('ignore')
import logging
import time


# -------------------------------
# Logging Configuration
# -------------------------------

os.makedirs("logs", exist_ok = True)

logging.basicConfig(
    filename = "logs/ingestion.db.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)


# -------------------------------
# Database Connection
# -------------------------------

engine = create_engine("sqlite:///retail.db")


# -------------------------------
# Function to Ingest Data
# -------------------------------

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)

def load_raw_data():
   
    start = time.time()
    
    for file in os.listdir(r'C:\Users\gaura\Retail_Sales_Analytics\data'):
        if '.csv' in file:
            df_raw = pd.read_csv(r'C:\Users\gaura\Retail_Sales_Analytics\data/' + file)
            df = df_raw.copy()
            
            logging.info(f'Ingesting {file} in db')
            
            print(file, df.shape)
            ingest_db(df, file[:-4], engine)
            
    end = time.time()
    total_time = (end - start)/60
    logging.info('------Ingestion Completed------')

    logging.info(f'\nTotal Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()

