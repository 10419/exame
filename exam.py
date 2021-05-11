class exam:
  def estCondicional01():
    print("UPeU")
    print("Bonificacion para el docente")
    sa=850
    Su=int(input("ingrese su sueldo:"))
    P=int(input("Ingrese la cantidada de puntos:"))
    P==0
    s=0
    if P>=50 and P<101:
      s=(sa*0.10)+Su
    elif P>=101 and P<151:
      s=(sa*0.40)+Su
    elif P>=151 :
      s=(sa*0.70)+Su
    else:
      print("verifique sus puntos")
    print("Su sueldo sueldo es de",s,", gracias por trabajar con nosotros") 
  estCondicional01()   