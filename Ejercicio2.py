#!/usr/bin/python
# -*- coding: -utf8 -*-
import math as m 
from turtle import * 
n1=4
n2=int(input("Número de lados del polígono: "))
for j in range(n1):
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
	setheading(j*(180-180*(n1-2)/n1))
	forward(200)
exitonclick()

