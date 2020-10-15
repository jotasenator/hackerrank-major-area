#problem solving intermedio hackerrank valido solo 3/15
#inputs demasiados valores

def datos(w,h,isVertical,distance):
	#primer cuadrado
	if isVertical[0]==0:
		area1=distance[0]*w
		area2=(h-distance[0])*w
		if area1<area2:
			area1=area2

		#4 areas
		if isVertical[1]==1:
			lista_area=[distance[1]*(h-distance[0]),
						(w-distance[1])*(h-distance[0]),
						(w-distance[1])*distance[0],
						distance[1]*distance[0]
						]
			lista_area.sort()

		#3 areas
		elif isVertical[1]==0:
			lista_area=[(h-distance[0])*w,
						(distance[0]-distance[1])*w,
						distance[1]*w
						]
			lista_area.sort()


	elif isVertical[0]==1:
		area1=h*(w-distance[0])
		area2=h*(distance[0])
		if area1<area2:
			area1=area2

		#4 areas
		if isVertical[1]==0:
			lista_area=[distance[0]*(h-distance[1]),
						(w-distance[0])*(h-distance[1]),
						(w-distance[0])*distance[1],
						distance[0]*distance[1]
						]

		#3 areas
		elif isVertical[1]==1:
			lista_area=[distance[0]*h,
						(w-(distance[0]+distance[1]))*h,
						distance[1]*h
						]
		lista_area.sort()
	

	return area1,lista_area[-1]



print(datos(5,4,[0,1],[3,1]))
print(datos(4,4,[0,1],[1,3]))
print(datos(4,4,[0,0],[3,1]))
print(datos(4,4,[1,1],[1,2]))
print(datos(5,4,[1,0],[1,3]))