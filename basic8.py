import re
file = open('bbc.txt')
trumpfile = open('Trump.txt', 'w')
hillaryfile = open('Hillary.txt', 'w')

for line in file:
    line = line.rstrip()
    if line.find('Trump') == -1: continue 
    trumpfile.write(line)
    if line.find('Hillary') == -1: continue
    hillaryfile.write(line)
    
trumpfile.close()
hillaryfile.close()


