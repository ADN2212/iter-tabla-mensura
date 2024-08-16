from math import atan, pi, atan, hypot

def calcular_GMS(angulo, c):
	if angulo < 0:
		angulo = -1 * angulo

	entero = 0
	decimal = 0
	GMS = [0, 0, 0]

	for i in range(3):
		entero = int(angulo)
		decimal = angulo - entero

		if entero < 10:
			GMS[i] = "0" + str(entero)
		else:
			GMS[i] = entero

		angulo = decimal * 60

	if c == 3:	
		return str(GMS[0]) + "°" + str(GMS[1]) + "'" + str(GMS[2]) + '"'

	elif c == 2:
		return str(GMS[0]) + "°" + str(GMS[1]) + "'" 
	
	elif c == 1:
		return str(GMS[0]) + "°"

	else:
		return None		

def rumbo_y_dist(punto_1, punto_2):
	delta_x = punto_2[1] - punto_1[1]
	delta_y = punto_2[2] - punto_1[2]
	distancia = round(hypot(delta_x, delta_y), 2)
	rumbo = "No definido"
 
	if delta_x > 0 and delta_y > 0:
		rumbo = "N {} E".format(calcular_GMS(atan(delta_x/delta_y)*(180/pi), 2))

	elif delta_x > 0 and delta_y < 0:
		rumbo = "S {} E".format(calcular_GMS(atan(delta_x/delta_y)*(180/pi), 2))

	elif delta_y < 0 and delta_y < 0:
		rumbo = "S {} W".format(calcular_GMS(atan(delta_x/delta_y)*(180/pi), 2))	

	elif delta_x < 0 and delta_y > 0:
		rumbo = "N {} W".format(calcular_GMS(atan(delta_x/delta_y)*(180/pi), 2))

	elif delta_x > 0 and delta_y == 0:
		rumbo = "N 90°00' E"
	
	elif delta_x == 0 and delta_y < 0:
		rumbo = "S 00°00' E"

	elif delta_x < 0 and delta_y == 0:
		rumbo = "N 90°00' W"
	
	elif delta_x == 0 and delta_y > 0:
		rumbo = "N 00°00' E"
  
	return (rumbo, round(distancia, 2))