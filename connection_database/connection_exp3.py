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
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM lqa, lqa1 WHERE (lqa.unique2 = lqa1.unique2) AND (lqa1.unique2 < 1000)) as A"""

conn.commit();
end_time = time.time()
print("time for query 9 = ", (end_time-start_time))

cur.execute("""DROP TABLE TMP""")
cur.execute("""DROP TABLE lqa""")
cur.execute("""DROP TABLE lqa1""")

conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO BPRIME FROM (SELECT * FROM lqa WHERE lqa.unique2 < 1000) as A""")

conn.commit();
end_time = time.time()
print("time for query 10 = ", (end_time-start_time))

cur.execute("""DROP TABLE BPRIME""")
cur.execute("""DROP TABLE lqa""")

conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
#lqa is power of ten less than same size lqa1 and lqa2
cur.execute("""SELECT INTO TMP (SELECT * FROM lqa, lqa1, lqa2 WHERE (lqa.unique2 = lqa1.unique2) AND (lqa1.unique2 = lqa2.unique2) AND (lqa1.unique2 < 1000)) as A""")


conn.commit();
end_time = time.time()
print("time for query 11 = ", (end_time-start_time))

cur.execute("""DROP TABLE TMP""")
cur.execute("""DROP TABLE lqa""")
cur.execute("""DROP TABLE lqa1""")
cur.execute("""DROP TABLE lqa2""")

conn.commit();
conn.close()
