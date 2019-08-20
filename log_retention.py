import os
import time
import datetime
import json

with open('/home/invlab/Desktop/Tasks Naman/log_retention_app.json','r') as config_file:   
    data = json.load(config_file)                            # Reading configuration file

path = data['path']                                          #Initializing variables using config file
extensions = data['extensions']

x = int(input("Enter the no.of days since last modification from which you want to delete the logs."))
files = []                                                   #Initializing the array for appending the file names in it

for r,d,f in os.walk(path):                                  #os.walk() returns the root, directories and files in the specified path
    for filess in f:                                         #Iterating in the directories
        for i in extensions:                                 #Iterating in the set
            if filess.endswith(i):                           #Checking for Extensions
                files.append(os.path.join(r,filess))         #Appending all files with particular extension

for f in files:
    modified = os.path.getmtime(f)                           # Getting time in seconds
    t = time.ctime(modified)                                 # Converting time to readable string form
    m = datetime.datetime.strptime(t,"%a %b %d %H:%M:%S %Y") # Converting time to datetime object
    current_time = datetime.datetime.today()                 # Getting the current time
    diff = current_time - m                                  # Calculating the difference

    if diff.days > x:                                        # Comparing the difference with our threshold
        os.remove(f)                                         # Deleting the file
        print(f"{f} removed from your system")               # Printing the message after deletion with the file name.
