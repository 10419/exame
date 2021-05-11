class examen:
  def estCondicional01():
    print("Aritmetica basica")
    a=int(input("ingrese su Numero1:"))
    b=int(input("ingrese su Numero2:"))
    print("operaciones")
    print("1=suma")
    print("2=resta")
    print("3=multiplicacion")
    print("4=dividion")
    print("5=potencia")
    x=int(input("elige una opcion:"))
    s=0
    if x>=1 and x<2:
      s=a+b
    elif x>=2 and x<3:
      s=a-b
    elif x>=3 and x<4:
      s=a*b
    elif x>=4 and x<5:
      s=a/b
    elif x>=5 and x<6:
      s=a^b
    else:
      print("la opcion ingresesada no existe")
    print("el resultado es:",s)
  estCondicional01()