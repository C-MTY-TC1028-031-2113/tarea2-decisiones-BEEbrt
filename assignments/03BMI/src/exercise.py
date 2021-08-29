peso = float (input("Su peso en kilogramos por favor : "))
altura = float(input ("Su altura en metros por favor: "))
IMC = peso / altura**2
print("IMC: " + str(IMC) )
if IMC<20:
        print ("Peso Bajo")
elif IMC <= 20 and IMC <= 25:
        print ("Normal")
elif IMC <= 25 and IMC <= 30:
        print ("Sobrepeso")
elif IMC <= 30 and IMC <= 40:
        print ("Obesidad")
elif IMC >= 40.00:
        print ("Obesidad Morbida")