import os
import subprocess
import psycopg2

print("create experiment:")
conn = psycopg2.connect(database='postgres', user='aditya', password='taco', host='127.0.0.1', port='5432')
cur = conn.cursor()
for i in range(7):
#    os.system('python3 connection_create1.py')
#    subprocess.call("./a.sh", shell=True)
#    os.system('python3 connection_create2.py')
#    subprocess.call("./a.sh", shell=True)
#    os.system('python3 connection_create3.py')
#    subprocess.call("./a.sh", shell=True)
#    os.system('python3 connection_create4.py')
#    subprocess.call("./a.sh", shell=True)

#    subprocess.call("./a.sh", shell=True)
#    os.system('python3 exp2.py')

    subprocess.call("./a.sh", shell=True)
    os.system('python3 exp3.py')

#    subprocess.call("./a.sh", shell=True)
#    os.system('python3 exp4_1.py')

#    subprocess.call("./a.sh", shell=True)
#    os.system('python3 exp5.py')

