#!/usr/bin/python
# -*- coding: -utf8 -*-
import math as m 
from turtle import * 
n1=int(input("Número de filas de la pirámide: "))
l=3
for j in range(n1):
	k=0	
	while k<=j:
		setheading(180/l-90)
		penup()
		forward(50)
		pendown()
		setheading(0)
		for i in range(l):
			left(180-180*(l-2)/(l))
			forward(50*(m.sin(m.pi/l)))
		left(90+180/l)
		penup()
		forward(50)
		setheading(0)
		forward(75*m.sqrt(3)/2)
		k+=1		
	setposition(-(j+1)*32.5*m.sqrt(3)/2,-(j+1)*75)
	l+=1
exitonclick()
