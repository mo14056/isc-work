 

#question 1

#using 2 terminal to get the file and copy it using cp and the link of my current directory

with open("weather.csv", "r") as reader: #"r" is the default you dont need to use it but you do with the rest so it is a good habbit

   data = reader.read()

print data
