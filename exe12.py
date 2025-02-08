#Escreva o programa que pergunte o valor total da conta em seguida pergunte quantos clientes existem,divida a conta pelos clintes e exiba o quanto cada cliente deve pagar seguida da mensage "cada clinte deve pagar: [x valor]"
valortotal=int(input("Qual o valor da compra: "))
totalclientes=int(input("Qual a quantidade de Clientes: "))
total=valortotal/totalclientes
print(valortotal/totalclientes)
print("Cada cliente tem q pagar: ",total)