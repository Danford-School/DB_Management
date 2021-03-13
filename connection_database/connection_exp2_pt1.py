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
cur.execute("""SELECT INTO TEMP FROM (SELECT DISTINCT two, four, ten, twenty, onePercent, string4 FROM lqa) as A""")

conn.commit();
end_time = time.time()
print("time = ", (end_time-start_time))

cur.execute("""DROP TABLE TEMP""")
cur.execute("""DROP TABLE lqa""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)



