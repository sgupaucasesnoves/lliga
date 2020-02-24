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

w=encriptar(frase)
print(w)
input("Premi intro per acabar")