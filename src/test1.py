
import datetime

# Get the current time
now = datetime.datetime.now()

# Print the current time

print ("Jonte test ------------------------------------------")
print("Current Time1:", now)

print("Current Time2:", now.strftime("%H:%M:%S"))

print("Current Time3:", now.strftime("%Y-%m-%d ---------------- %H:%M"))

print ("")

fruits = ["apple", "banana", "cherry","mango","Passion fruit"]
for x in fruits:
  print(x)

print ("")
inde_x = fruits.index ("banana")
print (inde_x )

print ("")
Vegetables = ["lettuce", "mushrom","potatoes","cucumber"]
for y in Vegetables:
  print (y)

print ("")
#print(x,y)



#display x:
print('print x:', x)

#convert to list to display the content of x:
print(list(x))
