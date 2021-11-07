# IMPORTING LIBRARIES #
from csv import reader
import pandas
import re

# GLOBAL VARIABLES #
regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
openfile = open('textfile.txt', 'w+')

# READING FILES + SAVING text COLUMN IN TEXT FILE#
with open('dataset.csv', 'r') as readobj:
    csvreader = reader(readobj, delimiter=',')
    for row in csvreader: 
        openfile.write(str(row))
openfile.close()

# USING ENTRIES IN text COLUMN #
file = open('textfile.txt', 'r+')

# PARSING THROUGH text COLUMN #
for line in file: 
    line = line.strip()
    x = re.findall(regex, line)
    
# PRINTING ALL FOUND URLS #
for p in x: 
    print(str(p)+'\r\n')  