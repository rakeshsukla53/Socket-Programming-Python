__author__ = 'rsukla'

def cracklepop():
     for i in range(1, 101):
         if i%3 == 0:
             print "Crackle"
         if i%5 == 0:
             print "Pop"
         if (i%3 == 0) and (i%5 == 0):
             print "Cracklepop"
         else:
             print i

cracklepop()

