class exa:
  def estCondicional01():
    print("UPeU")
    print("Fundamentos de Programaion")
    n=int(input("ingrese su nota, primera unidad:"))
    n1=int(input("ingrese su nota, segunda unidad:"))
    n2=int(input("ingrese su nota, tercera unidad:"))
    n3=int(input("ingrese su nota, trabajo final:"))
    n01=n*0.20
    n02=n1*0.15
    n03=n2*0.15
    n04=n3*0.50
    pro=(n01+n02+n03+n04)
    print("La nota del alumno es de",pro)
    if pro>=20:
      print("Sigue asi llegaras muy lejos")
    else:
      print("esfuerzate")
  estCondicional01()
