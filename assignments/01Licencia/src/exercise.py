edad= int(input("Ingresa tu edad: "))
if edad>=18:
 print("Eres mayor de edad ")
 id= (input("¿Tienes identificacion oficial?"))
 if id=="si":
        print("Tramite de licencia concedido ")
 else:
    print("tramite de licencia denegado")
else:
    print("No cumples con los requisitos")
