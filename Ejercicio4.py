#!/usr/bin/python
# -*- coding: -utf8 -*-
import math as m 
from turtle import * 
n2=int(input("Número de lados del polígono: "))
n1=int(input("Número de filas de la pirámide: "))
for j in range(n1):
	k=0
	while k<=j:
		setheading(180/n2-90)
		penup()
		forward(25/(m.sin(m.pi/n2)))
		pendown()
		setheading(0)
		for i in range(n2):
			left(180-180*(n2-2)/n2)
			forward(50)
		left(90+180/n2)
		penup()
		forward(25/(m.sin(m.pi/n2)))
		setheading(0)
		forward(100*m.sqrt(3)/2)
		k+=1
	setposition(-(j+1)*50*m.sqrt(3)/2,-(j+1)*100)
exitonclick()

