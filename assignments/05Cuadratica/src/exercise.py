inca=int(input("Da el valor de a: "))
incb=int(input("Da el valor de b: "))
incc=int(input("Da el valor de c: "))
discrimintante= (incb**2)-(4*inca*incc)
chicharronero1= (-incb + discrimintante) / 2*inca
chicharronero2= (-incb - discrimintante) / 2*inca
if chicharronero1 == 0:
    print("No tiene solucion")
elif chicharronero2 == 0:
    print ("No tiene solucion")
if discrimintante < 0: 
    print("Raices complejas")
else :
    print ( chicharronero1 )
    print ( chicharronero2 ) 
if inca == 0 and incb != 0: 
    x = (- incc / incb)
    print (x)
