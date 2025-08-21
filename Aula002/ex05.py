#Faça um Programa que peça
#  uma data no formato dd/mm/aaaa
#  e determine se a mesma é uma data válida

# data = input("Digite uma data no formato dd/mm/aaaa: ")
# print(data.split("/"))



# palca = "ABC-1234"
# print(palca)

# letras = palca[:3]
# print(letras)


# numeros = palca[4:8]
# print(numeros)


datatexto = "23/02/2025"

dia = int(datatexto[0:2])
mes = int(datatexto[3:5])
ano = int(datatexto[6:10])

print(datatexto.split("/"))

dia = int(datatexto.split("/")[0])
mes = int(datatexto.split("/")[1])
ano = int(datatexto.split("/")[2])





# if (ano < 0):
#     print("Ano invalido")

# if(mes > 12 and mes <1):
#     print("mes invalido")

#     if((mes == 1) or (mes == 3) or  (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or  (mes == 12) ):
#         if(dia > 31 and dia <1):
#             print("dia invalido")
    
#     if((mes == 4) or (mes == 6) or  (mes == 9) or (mes == 11) ):
#         if(dia > 30 and dia <1):
#             print("dia invalido")
      
#     if((mes ==2) and (ano % 4 == 0 and ano % 100 != 0) ):
#         if(dia > 29 and dia <1):
#             print("dia invalido")
     


