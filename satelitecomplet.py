#Satélite orbitando la Tierra.
#1) Calcule la altura sobre la superficie (h) terrestre a la que debe estar un satélite que órbita la Tierra con período T.
print("1.Altura sobre la superficie terrestre a la que debe estar un satélite es h=(((g*m*T**2)/4*pi**2)**1/3)-r")

#2) Escriba un programa que estime h a partir de un período dado.

print("2.codigo de la orbita de un satelite")
g=6.67e-11
m=5.97e24
r=6371000
pi=3.1416
T=float(input("ingrese el valor para el periodo"))
h=(((g*m*T**2)/4*pi**2)**1/3)-r
print("el valor de la altura del satelite es:",h)

#3) Estime la altura para un T de un día (geosincrónico), 90 min y 45 min

print("3.la altura para un T de un día (geosincrónico), 90 min y 45 min")
t1=86400
t2=5400
t3=2700
h1=(((g*m*t1**2)/4*pi**2)**1/3)-r
h2=(((g*m*t2**2)/4*pi**2)**1/3)-r
h3=(((g*m*t3**2)/4*pi**2)**1/3)-r
print("el valor de la altura del satelite en 1 hora es:",h1)
print("el valor de la altura del satelite en 90 min es:",h2)
print("el valor de la altura del satelite en 45 min es:",h3)

#4) Técnicamente, el período T de un sátelite geosincrónico es por día sideral (23.93 h). Cuánta es la diferencia en h?

print("4.diferencia en la altura")
t4=86148
h4=(((g*m*t4**2)/4*pi**2)**1/3)-r
h5=h1-h4
print("la diferencia en la altura es:",h5)



