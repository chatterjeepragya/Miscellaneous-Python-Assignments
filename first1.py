m = ""
array = []
n=0
while m != "done":
    m = input("Enter a number, when you are done, enter 'done': ")
    if m.isdigit() == True :
        array.append(int(m))
        n = n + 1
    elif m.isdigit()== False and m!= "done":
        print("Invalid input")

print("The total valid numbers entered:" + str(n))
print("The sum of the numbers:" + str(sum(array)))
print("The maximum of the numbers:" + str(max(array)))
print("The minimum of the numbers:" + str(min(array)))
print("The average of the numbers:" + str(sum(array) / n))


