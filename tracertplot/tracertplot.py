
import sys
import subprocess
import time

print (sys.argv[0], sys.argv[1])

if (len(sys.argv) < 1):
    print ("usage: tracertplot.py <destination ip>")

def subprocess_cmd(command):
    process = subprocess.Popen('tracert -w 100 www.google.com',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    for line in iter(process.stdout.readline,""):
        print(line)

subprocess_cmd('tracert -w 100 www.google.com')
time.sleep(1)
subprocess_cmd('tracert -w 100 www.google.com')
time.sleep(1)
subprocess_cmd('tracert -w 100 www.google.com')
time.sleep(1)
subprocess_cmd('tracert -w 100 www.google.com')