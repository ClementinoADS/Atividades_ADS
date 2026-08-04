#Verificador de atividades

dia = str(input('Qual o dia da semana é hoje? '))

if dia == "Sábado" or dia == "Domingo":
    print("Hoje você não precisa estudar")

elif dia == "Segunda" or dia == "Quarta" or dia == "Sexta":
    print("Hoje você precisa estudar das 14h até 19h")

elif dia == "Terça" or dia == "Quinta":
    print("Hoje você precisa treinar na academia as 15h")

else:
    print("Não entendi qual dia da semana é.")



