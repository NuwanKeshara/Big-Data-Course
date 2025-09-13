import mysql.connector
import pandas as pd
import logging
from tqdm import tqdm

# Database connection details
DB_CONFIG = {
    'host': '34.122.208.22',
    'user': 'root',
    'password': 'BigData@12345',
    'database': 'loan_data',
    'table_name': 'credit_record'
}



csv_file_path = 'Data_ingestion/credit-card-approval-prediction/credit_record.csv'

df = pd.read_csv(csv_file_path)
print(df.head())

# curl ifconfig.me

# try:
#     # Connect to MySQL database
#     conn = mysql.connector.connect(
#         host=DB_CONFIG['host'],
#         user=DB_CONFIG['user'],
#         password=DB_CONFIG['password'],
#         database=DB_CONFIG['database']
#     )
#     cursor = conn.cursor()
    
#     # Create table if not exists
#     create_table_query = f'''
#     CREATE TABLE IF NOT EXISTS {DB_CONFIG['table_name']} (
#         ID VARCHAR(50),
#         MONTHS_BALANCE INT,
#         STATUS VARCHAR(10),
#         PRIMARY KEY (ID, MONTHS_BALANCE)
#     ) ENGINE=InnoDB;
#     '''
#     cursor.execute(create_table_query)
#     conn.commit()
#     logging.info("Table `credit_record` created successfully (if not already exists).")
    
# except Exception as e:
#     logging.error(f"Error creating table: {e}")
# finally:
#     cursor.close()
#     conn.close()


# import mysql.connector
# import logging
# from tqdm import tqdm


# try:
#     # Reconnect to MySQL
#     conn = mysql.connector.connect(
#         host=DB_CONFIG['host'],
#         user=DB_CONFIG['user'],
#         password=DB_CONFIG['password'],
#         database=DB_CONFIG['database']
#     )
#     cursor = conn.cursor()
    
#     # Insert Data in Batches
#     batch_size = 1000
#     insert_query = f"""INSERT INTO {DB_CONFIG['table_name']} (ID, MONTHS_BALANCE, STATUS) 
#                       VALUES (%s, %s, %s) 
#                       ON DUPLICATE KEY UPDATE STATUS=VALUES(STATUS)"""  # Avoid duplicates
    
#     records = df.to_records(index=False)
#     records_list = [(str(record[0]), int(record[1]), str(record[2])) for record in records]  # Convert records to tuples with native Python types
    
#     for i in tqdm(range(0, len(records_list), batch_size)):
#         batch = records_list[i:i+batch_size]
#         cursor.executemany(insert_query, batch)
#         conn.commit()
#         logging.info(f"Inserted {i + len(batch)} records so far...")
    
#     logging.info("Data upload completed successfully!")

# except mysql.connector.Error as e:
#     logging.error(f"MySQL error: {e}")
# except Exception as e:
#     logging.error(f"Error inserting data: {e}")
# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()


try:
    # Reconnect to MySQL
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )
    cursor = conn.cursor()
    
    # Count Records
    cursor.execute(f"SELECT COUNT(*) FROM {DB_CONFIG['table_name']}")
    record_count = cursor.fetchone()[0]
    print(f"Total records in `{DB_CONFIG['table_name']}`: {record_count}")
    
except Exception as e:
    print(f"Error verifying data: {e}")
finally:
    cursor.close()
    conn.close()

