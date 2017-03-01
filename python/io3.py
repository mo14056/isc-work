

#question 3

with open("weather.csv", "r") as reader:

  #data = reader.read()

#print data


 line = reader.readline()

 rain = [] #create an empty list

 for line in reader.readline(): #for loop
        print line

 
