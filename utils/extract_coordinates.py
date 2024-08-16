from io import open
from tkinter import messagebox
import re

def extract_coords_from_pm(direc):
	with open(direc, encoding = 'utf-8') as f:
		lineas = f.readlines()
		coords = []

		while lineas[len(lineas) - 1] == '\n':
			lineas.pop()

		if not lineas[0] == "AutoCAD-MIM por FeloCAD\n":
			messagebox.showwarning('Error', f'El archivo ingresado no cumple con el formato.\nRevise: {direc}.')
			return False

		for i in range(1, len(lineas)):
			try:
				este, norte = lineas[i].split()
				coords.append((round(float(este), 3),  round(float(norte), 3)))
			except ValueError:
				messagebox.showwarning('Error', f'Hay un error en la linea No.{"0" + str(i) if i < 10 else i}, verifique que esta no haya sido alterada.\nRevise: {direc}')
				return False

		while coords[0][0] == coords[len(coords) - 1][0] and coords[0][1] == coords[len(coords) - 1][1]:
			coords.pop()

		return coords


def extrac_coord_from_list(direc):
	with open(direc, encoding = 'utf-8') as f:
		lineas = f.readlines()
		coords = []
		while lineas[len(lineas) - 1] == '\n':
			lineas.pop()

		for i in range(len(lineas)):
			linea = lineas[i]
			if "X" in linea and "Y" in linea and "Z" in linea:
				pos_x = re.search("X", linea).span()[0]
				pos_y = re.search("Y", linea).span()[0]
				pos_z = re.search("Z", linea).span()[0]
				este = ""
				norte = ""
    
				for j in range(pos_x, pos_y):
					if linea[j].isdigit() or linea[j] == ".":
						este += linea[j]

				for k in range(pos_y, pos_z):
					if linea[k].isdigit() or linea[k] == ".":
						norte += linea[k]	

				try:
					este = round(float(este), 3)
					norte = round(float(norte), 3)
					coords.append((este, norte))

				except ValueError:
					messagebox.showwarning('Error', f'La linea No {"0" + str(i + 1) if i < 10 else i + 1} no cumple con el formato.\nRevise: {direc}')	
					return False
				
			else:
				messagebox.showwarning('Error', f'La linea No {"0" + str(i + 1) if i < 10 else i + 1} no cumple con el formato.\nRevise: {direc}')	
				print(linea)
				return False

		while coords[0][0] == coords[len(coords) - 1][0] and coords[0][1] == coords[len(coords) - 1][1]:
			coords.pop()

		return coords
