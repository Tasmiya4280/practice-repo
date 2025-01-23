import os

def os_commands(command):
    print (os.system(command))

def run_commands(command):
    return os.system(command)



os_commands("uptime")
os_commands("date")
os_commands("ls -ltr")
run_commands("df -h")