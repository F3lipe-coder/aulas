#strings


# string permite simbolos como @#$%¨&*"(

# string

#texto="Felipe"
# todas index começa de 0123456
#print(texto[4:])# Atribui


#input| convert| output
texto=" Luis Felipe"
print(texto.upper())
texto= texto.upper()
print(texto)
print(texto.lower())

texto=input("Digite seu nome")
texto=texto.lower()
print(texto.title())
print("#"*30)

texto="    Felipe Alves/joa/souza"
print(texto.strip())
resposta=input("Deseja entrar no sistema sim ou não?").strip()[0].upper()
#if resposta== "S"
 print("Entrou!")
print(texto.strip().count("o"))

print(texto.count("F"))
print(texto.strip().index("g"))
lista=texto.split("/")
print(lista)
lista=texto.split()




