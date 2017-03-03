
#question 3

def calc_hypo(a, b): #def a function with 2 arguments

   if type(a) not in (int,float) or type(b) not in (int,float):
     print "bad argument"
     return false

   if a <=0 or b<=0:
     print "bad argument"
     return false


   hypo = (a**2 + b**2)**0.5
   return hypo
   


print calc_hypo(0, -2)
