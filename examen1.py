class examen1:
  def estCondicional01():
    print("Hospital")
    e=int(input("ingrese su edad:"))
    print("sexo")
    print("1=varon")
    print("2=mujeer")
    s=int(input("ingrese su sexo:"))
    if e>=70:
      print("la persona recibe la vacuna C")
    elif e>=16 and e<70 and s==2:
      print("la persona recibe la vacuna B")
    elif e>=16 and e<70 and s==1:
      print("la persona recibe la vacuna A")
    else :
      print("la persona recibe la vacuna A")
  estCondicional01()