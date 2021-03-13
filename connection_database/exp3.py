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

subprocess.call("./a.sh", shell=True)
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM tenk lqa, tenk lqa1 WHERE (lqa.unique2 = lqa1.unique2) AND (lqa1.unique2 < 1000)) as A""")

conn.commit();
end_time = time.time()
print("ex3,q9,10k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM hundredk lqa, hundredk lqa1 WHERE (lqa.unique2 = lqa1.unique2) AND (lqa1.unique2 < 1000)) as A""")

conn.commit();
end_time = time.time()

print("ex3,q9,100k", ((end_time-start_time)*1000))
cur.execute("""DROP TABLE TMP""")

conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM five_hundredk lqa, five_hundredk lqa1 WHERE (lqa.unique2 = lqa1.unique2) AND (lqa1.unique2 < 1000)) as A""")

conn.commit();
end_time = time.time()
print("ex3,q9,500k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""CREATE TABLE BPRIME(
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

conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""INSERT INTO BPRIME (SELECT * FROM tenk WHERE tenk.unique2 < 1000)""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM tenk, BPRIME WHERE tenk.unique2 = BPRIME.unique2) as A""")
conn.commit();
end_time = time.time()
print("ex3,q10,10k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")
cur.execute("""DROP TABLE BPRIME""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""CREATE TABLE BPRIME(
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
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""INSERT INTO BPRIME (SELECT * FROM hundredk WHERE unique2 < 1000)""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM hundredk, BPRIME WHERE hundredk.unique2 = BPRIME.unique2) as A""")

conn.commit();
end_time = time.time()
print("ex3,q10,100k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE BPRIME""")
cur.execute("""DROP TABLE TMP""")

conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""CREATE TABLE BPRIME(
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
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""INSERT INTO BPRIME (SELECT * FROM five_hundredk WHERE unique2 < 1000)""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM five_hundredk, BPRIME WHERE five_hundredk.unique2 = BPRIME.unique2) as A""")
conn.commit();
end_time = time.time()
print("ex3,q10,500k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE BPRIME""")
cur.execute("""DROP TABLE TMP""")

conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
#lqa is power of ten less than same size lqa1 and lqa2
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM onek lqa, tenk lqa1, tenk lqa2 WHERE (lqa.unique2 = lqa1.unique2) AND (lqa1.unique2 = lqa2.unique2) AND (lqa1.unique2 < 1000)) as A""")

conn.commit();
end_time = time.time()
print("ex3,q11,10k-1k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")

conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
#lqa is power of ten less than same size lqa1 and lqa 2
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM tenk lqa, tenk lqa1, hundredk lqa2 WHERE (lqa.unique2 = lqa1.unique2) AND (lqa1.unique2 = lqa2.unique2) AND (lqa1.unique2 < 1000)) as A""")

conn.commit();
end_time = time.time()
print("ex3,q11,100k-10k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")

conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
#lqa is power of ten less than same size lqa1 and lqa2
cur.execute("""SELECT INTO TMP FROM (SELECT * FROM hundredk lqa, five_hundredk lqa1, five_hundredk lqa2 WHERE (lqa.unique2 = lqa1.unique2) AND (lqa1.unique2 = lqa2.unique2) AND (lqa1.unique2 < 1000)) as A""")

conn.commit();
end_time = time.time()
print("ex3,q11,500k-100k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TMP""")

conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)
