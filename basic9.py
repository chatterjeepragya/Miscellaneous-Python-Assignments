### importing libraries
import string
import glob
import os

### opening two read and write text files 
# defining global variables
file = open('wordcounts.txt', 'w+')
file1 = open ('mainfile.txt', 'w+')
arr = os.listdir('.')
wordlist = list() # list to split lines

### reading all files and writing them into mainfile

fhand = open('abc.txt')
for line in fhand:
    file1.write(line)
    
fhand1 = open('bbc.txt')  
for line1 in fhand1:
    file1.write(line1)
    
fhand2 = open('cnn.txt')
for line2 in fhand2:
    file1.write(line2)
        
fhand3 = open('fox.txt')
for line3 in fhand3:
    file1.write(line3)
        
fhand4 = open('msnbc.txt')
for line4 in fhand4:
    file1.write(line4)
        
fhand5 = open('newsok.txt')
for line5 in fhand5:
    file1.write(line5)
        
fhand6 = open('usatoday.txt')
for line6 in fhand6:
    # test: print(line6)
    file1.write(line6)
    
fhand7 = open('usnews.txt')
for line7 in fhand7:
    file1.write(line7)

### news files are now collated into one main file 

wordfrequency = [] # list to save frequency
file1.close()

mainfile1 = open('mainfile.txt', 'r+')

### creating list of words from mainfile 
for mainline in mainfile1:
    #test: print(mainline)
    mainline = mainline.strip() 
    mainline = mainline.translate (mainline.maketrans('','', string.punctuation))
    mainline = mainline.lower()
    wordlist = mainline.split() # note: fix that
 
# test: print (wordlist)

### counting frequency
for w in wordlist: 
    wordfrequency.append(wordlist.count(w))
    #test: print(wordfrequency)

file.write(str(list(zip(wordlist, wordfrequency))))
# test: print(file)
# test: print(file1)

mainfile1.close()
file.close()