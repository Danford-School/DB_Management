
import psycopg2
import argparse
import re
import csv
import os
import subprocess
import time


start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT DISTINCT two, four, ten, twenty, onePercent, string4 FROM tenk) as A""")

conn.commit();
end_time = time.time()
print("ex2,q18,tenk", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT DISTINCT two, four, ten, twenty, onePercent, string4 FROM hundredk) as A""")

conn.commit();
end_time = time.time()
print("ex2,q18,100k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT DISTINCT two, four, ten, twenty, onePercent, string4 FROM five_hundredk) as A""")

conn.commit();
end_time = time.time()
print("ex2,q18,500k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)



start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT DISTINCT two, four, ten, twenty, onePercent, tenPercent, twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4 FROM tenk) as A""")

conn.commit();
end_time = time.time()
print("ex2,q19,10k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)


start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT DISTINCT two, four, ten, twenty, onePercent, tenPercent, twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4 FROM hundredk) as A""")

conn.commit();
end_time = time.time()
print("ex2,q19,100k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)


start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT DISTINCT two, four, ten, twenty, onePercent, tenPercent, twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4 FROM five_hundredk) as A""")

conn.commit();
end_time = time.time()
print("ex2,q19,500k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)
