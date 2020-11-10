'''
filename: lab3q3.py
description: lab3q3
date: nov 6, 2020
author: Au Tsz Yui
'''
import math

# x**2 - 1 = 0
a = float(input('enter a:'))
b = float(input('enter b:'))
c = float(input('enter c:'))

x1 = (-b + math.sqrt(b*b- 4*a*c)) / (2*a) 

x2 = (-b - math.sqrt(b*b- 4*a*c)) / (2*a)

print(x1,x2)
print('%.5f.10f'%(x1, x2))
