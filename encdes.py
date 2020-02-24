clau='PAUCASESNOVES'
codi=list(clau)
frase=input("Quina frase voleu encriptar? ")

# encriptació
def encriptar(f):
  sortida=''
  for i in f:
    if i in clau:
      sortida+=str(codi.index(i))
    else:
      sortida+=i
  return(sortida)

# desencriptació (no funciona)
def desencriptar(f):
  texte=''
  for i in f:
    if i.isdigit():
      texte+=codi[int(i)]
    else:
      texte+=i
  return(texte)

w=encriptar(frase)
print(w)
print(desencriptar(w))
input()d