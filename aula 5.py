#while--> é o mesmo que o enquanto
#=0
#hile  i<=10
 #   print("Valor de i?",i)
 #   i+=1


#hile True:

#    resposta=input("Deseja sai do sistema sim ou não").strip()[0].lower()

#if resposta=="n":# entro na condição
#       break #posso quebrar meu loop

#nm=input("Digite nome")
#idade=input("Sua idade:")







#while  i<=10
  #  print("Valor de i?",i)
 #   i+=1
#

  #  resposta=input("Deseja sai do sistema sim ou não").strip()[0].lower()

#if resposta=="n":# entro na condição
#       break #posso quebrar meu loop

#while True:
  #  nome=input("Digite seu nome:")
  #  idade=int(input("Digite seu nome:"))

#    if idade>18:
   #     break
     #   print("Acabou o sistema!")



#nome=input("Digite seu nome:")
#idade=input("Digite sua idade:")
#if  str.isdigit(nome.replace(".","")) or  str.isdigit(idade.replace(".",""))
#while True:

 #   nota1=float(input("Digite sua nota:"))
#    nota2=float(input("Digite sua nota:"))
 #   nota3=float(input("digite sua nota:"))
 #   nota4=float(input("Digite sua nota:"))
 #   media=(nota1+nota2+nota3+nota4)/4
  #  print(media)
 #   if media>=8:
  #      break

#print("Você foi aprovado!")



#Trabalhando a validação

#n="12"
#print(n.isdigit()) #---> valida dados se for letra com true
#idade=input("Digite sua idade: ")
#print(idade.isdigit())

#print(idade.isnumeric())# valida dados que
#nome=input("Digite seu nome:")
#print(nome.isalpha())

#trocar o valor de um caracter eu posso usar o metodo o metodo replace ([vai procurar o valor que deseja mudar])
#decimal="12,45s"
#if str.isdigit(decimal.replace(".","")):
#    decimal=float(decimal)
#    print(type(decimal))
#else:
#    print(decimal)

#if  str.isdigit(decimal.replace(".","")) or  str.isdigit(decimal.replace(".","")):


while True:
    nome = input("Digite o nome do aluno: ")

    # Verifica se o nome é uma string
    if not nome.isalpha():
        print("Nome inválido. O nome deve conter apenas letras. Tente novamente.")
        continue  # Volta ao início do loop

    idade = input("Digite a idade do aluno: ")

    # Tenta converter a idade para um número inteiro
    try:
        idade = int(idade)
    except ValueError:
        print("Idade inválida. A idade deve ser um número inteiro. Tente novamente.")
        continue  # Volta ao início do loop

    notas = []
    for i in range(4):
        nota = input(f"Digite a nota {i + 1} do aluno: ")

        # Tenta converter a nota para um número float
        try:
            nota = float(nota)
        except ValueError:
            print("Nota inválida. A nota deve ser um número real. Tente novamente.")
            continue  # Volta ao início do loop

        notas.append(nota)

    # Calcula a média das notas
    media = sum(notas) / len(notas)

    if media > 8:
        print(f"{nome} foi aprovado com média {media:.2f}.")
        break  # Sai do loop
    else:
        print(f"{nome} não atingiu a média necessária para aprovação ({media:.2f}). Tente novamente.")

































