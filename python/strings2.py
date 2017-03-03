
#question2

s = "I love to write python"

split_s = s.split() #split the string into a list of words

print split_s

for word in split_s: # loop through the list of words
   
   if word.find("i") > -1:

      print "I found 'i' in: {0}".format(word) 


for word in split_s:

   if "i" in word:
 
      print "I found 'i' in '{0}'".format(word) #display of result is different
 

    
   


