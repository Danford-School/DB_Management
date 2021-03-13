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
cur.execute("""SELECT INTO TEMP FROM (SELECT min(unique2) FROM tenk) as A""")

conn.commit();
end_time = time.time()
print("ex5,q20,10k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)


start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT min(unique2) FROM hundredk) as A""")
conn.commit();
end_time = time.time()
print("ex5,q20,100k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)


start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT min(unique2) FROM five_hundredk) as A""")
conn.commit();
end_time = time.time()
print("ex5,q20,500k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)


start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT * INTO TEMP FROM (SELECT onePercent, min(unique3) FROM tenk AS stuff GROUP BY onePercent) as A """)
conn.commit();
end_time = time.time()
print("ex5,q21,10k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT min(unique3), onePercent FROM hundredk AS stuff GROUP BY onePercent) as A """)
conn.commit();
end_time = time.time()
print("ex5,q21,100k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT min(unique3), onePercent FROM five_hundredk AS STUFF GROUP BY onePercent) as A""")
conn.commit();
end_time = time.time()
print("ex5,q21,500k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT sum(unique3), onePercent FROM tenk as stuff GROUP BY onePercent) as A""")
conn.commit();
end_time = time.time()
print("ex5,q22,10k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT sum(unique3), onePercent FROM hundredk as stuff GROUP BY onePercent) as A""")
conn.commit();
end_time = time.time()
print("ex5,q22,100k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)

start_time = time.time()
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
cur.execute("""SELECT INTO TEMP FROM (SELECT sum(unique3), onePercent FROM five_hundredk AS stuff GROUP BY onePercent) as A""")
conn.commit();
end_time = time.time()
print("ex5,q22,500k", ((end_time-start_time)*1000))

cur.execute("""DROP TABLE TEMP""")
conn.commit();
conn.close()
subprocess.call("./a.sh", shell=True)
