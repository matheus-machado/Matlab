#!/usr/bin/env python3

import matplotlib.pyplot as plt

file_path = "GPS-15-25.csv"


log_file = open(file_path, "r")

lines = log_file.readlines()


latitude   = [] 
longitude  = []
velocidade = []

for line in lines[1:]:

	line = line.split(';')

	lat_aux  = line[0].split('.')
	long_aux = line[1].split('.')

	if(float(lat_aux[0][:-2]) < 0):
		latitude.append(-(float(lat_aux[0][:-2]) + (float(lat_aux[0][-2:]) + 1e-6*float(lat_aux[1]))/60))
	else:
		latitude.append(float(lat_aux[0][:-2]) + (float(lat_aux[0][-2:]) + 1e-6*float(lat_aux[1]))/60)
	
	if(float(long_aux[0][:-2]) > 0):
		longitude.append(-(float(long_aux[0][:-2]) + (float(long_aux[0][-2:]) + 1e-6*float(long_aux[1]))/60))
	else:
		longitude.append(float(long_aux[0][:-2]) + (float(long_aux[0][-2:]) + 1e-6*float(long_aux[1]))/60)
	
	velocidade.append(line[2])


plt.scatter(longitude, latitude)
plt.show()