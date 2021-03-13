import psycopg2
import argparse
import re
import csv
import os
import subprocess
import time

start_time = time.time()
user1 = 'aditya'
pass1 = 'taco'
db_name = 'postgres'

conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""CREATE TABLE lqa(
        unique1 INTEGER NOT NULL, 
        unique2 INTEGER NOT NULL,
        two INTEGER NOT NULL, 
        four INTEGER NOT NULL, 
        ten INTEGER NOT NULL, 
        twenty INTEGER NOT NULL, 
        onePercent INTEGER NOT NULL,
        tenPercent INTEGER NOT NULL, 
        twentyPercent INTEGER NOT NULL, 
        fiftyPercent INTEGER NOT NULL, 
        unique3 INTEGER NOT NULL, 
        evenOnePercent INTEGER NOT NULL, 
        oddOnePercent INTEGER NOT NULL, 
        stringu1 VARCHAR(52),
        stringu2 VARCHAR(52), 
        string4 VARCHAR(52))""")
cur.execute("""COPY lqa FROM '/home/asharoff/THE_5MTUP1.csv' DELIMITER ',' CSV HEADER""")

conn.commit();
end_time = time.time()
print("ex1,create,5m", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE lqa""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)



