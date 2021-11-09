


def sin_reprtidos (A,b):

  n=(int(b)-int(A))+1 
  a=A
  a2=A
  contador=0
  contador2=0
  aint=int(A) 

  for i in range(n):

    cero=a.count("0") 
    uno=a.count("1")
    dos=a.count("2")
    tres=a.count("3")
    cuatro=a.count("4")
    cinco=a.count("5")
    seis=a.count("6")
    siete=a.count("7")
    ocho=a.count("8")
    nueve=a.count("9")
    aint=aint+1 

    a=str(aint)

    if cero > 1  or uno > 1 or dos > 1 or tres > 1 or cuatro >1 or cinco > 1 or seis > 1 or siete > 1 or ocho > 1 or nueve > 1:
     contador=contador+1 
  

  print ("la cantidad de numeros que cumple la condicion son: ",n-contador)
  

  aint=int(A) 
  

  for i in range(n):
    cero=a2.count("0")
    uno=a2.count("1")
    dos=a2.count("2")
    tres=a2.count("3")
    cuatro=a2.count("4")
    cinco=a2.count("5")
    seis=a2.count("6")
    siete=a2.count("7")
    ocho=a2.count("8")
    nueve=a2.count("9")

  
    if cero > 1 or uno > 1 or dos > 1 or tres > 1 or cuatro >1 or cinco > 1 or seis > 1 or siete > 1 or ocho > 1 or nueve > 1:
     contador2=contador2+1
    else:
     print(a2)

    aint=aint+1
    a2=str(aint)

    

  return 

A=(input("digite a"))
b=(input("digite b"))
sin_reprtidos(A,b)
  



