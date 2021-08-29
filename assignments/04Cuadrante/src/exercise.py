grados= float(input(" Introduce los grados: "))
if grados == 0:
        print ("Sin cuadrante")
elif grados >= 1 and grados <= 90:
        print ("Primer cuadrante")
elif grados >= 91 and grados <= 180:
        print ("Segundo cuadrante")
elif grados >=181 and grados <= 270:
        print ("Tercer cuadrante")
elif grados >=271 and grados <= 360:
        print ("Cuarto cuadrante")