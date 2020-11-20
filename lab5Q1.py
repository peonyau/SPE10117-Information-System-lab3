'''
filename: circleArea.py             
                                                     
This program asks the user to input a
number for the radius of a circle.  The program     
then calculates and output the area of the circle.
'''
import math
import sys

def computeArea(r):
    return math.pi * r * r

def main():
 
    area = computeArea(float(sys.argv[1]))

    sys.stdout.write("The radius you provided was " + format(float(sys.argv[1]),'.2f') +
                " feet and the area is about " + format(area,'.12f') + " sq feet")

if __name__== "__main__" :
    sys.argv=[sys.argv[0],'1.0']
    main()
