
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
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM onek o, tenk a, tenk b WHERE ((o.unique2 = a.unique2) AND (a.unique2 = b.unique2) AND (b.unique2 < 100))) as A""")

conn.commit();
end_time = time.time()
print("ex4,q11,10k-1k", ((end_time-start_time)*1000))


cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM tenk o, hundredk a, hundredk b WHERE ((o.unique2 = a.unique2) AND (a.unique2 = b.unique2) AND (b.unique2 < 100))) as A""")

conn.commit();
end_time = time.time()
print("ex4,q11,100k-10k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM hundredk o, five_hundredk a, five_hundredk b WHERE ((o.unique2 = a.unique2) AND (a.unique2 = b.unique2) AND (b.unique2 < 100))) as A""")

conn.commit();
end_time = time.time()
print("ex4,q11,500k-100k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM tenk a, tenk b WHERE ((a.unique1 = b.unique1) AND (b.unique2 < 100))) as A""")

conn.commit();
end_time = time.time()
print("ex4,q15,10k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM hundredk a, hundredk b WHERE ((a.unique1 = b.unique1) AND (b.unique2 < 100))) as A""")

conn.commit();
end_time = time.time()
print("ex4,q15,100k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM five_hundredk a, five_hundredk b WHERE ((a.unique1 = b.unique1) AND (b.unique2 < 100))) as A""")

conn.commit();
end_time = time.time()
print("ex4,q15,500k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT DISTINCT two, four, ten, twenty, onePercent, tenPercent, twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4 FROM tenk) as A""")

conn.commit();
end_time = time.time()
print("ex4,q19,10k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT DISTINCT two, four, ten, twenty, onePercent, tenPercent, twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4 FROM hundredk) as A""")

conn.commit();
end_time = time.time()
print("ex4,q19,100k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT DISTINCT two, four, ten, twenty, onePercent, tenPercent, twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4 FROM five_hundredk) as A""")

conn.commit();
end_time = time.time()
print("ex4,q19,500k", ((end_time-start_time)*1000))
start_time = time.time()

cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

