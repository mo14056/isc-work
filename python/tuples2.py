
#question 2

mylist = [23,"hi", 2.4e-10]

for item in mylist: #for loop
   print item, mylist.index(item)

for (count,item) in enumerate(mylist):
   print count, item
