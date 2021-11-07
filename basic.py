data = input("Please enter a sentence containing an email address:")
str1 = data.find('@')
str3 = data.find(' ', str1)
if str3 == -1:
    length = len(data)
else:
    length = str3
for char in data[0 : str1]:
    m = data.rfind(" ")
print (data[m+1:length])



