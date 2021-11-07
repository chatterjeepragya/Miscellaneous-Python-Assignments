import re
file = open('wos.txt')
newfile = open('emails.txt', 'w')
for line in file:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(str(x))
        newfile.write(str(x))
newfile.close()
