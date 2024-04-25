#IMC = Peso / (altura * altura )
print("Academia MC Valinhos")
print(".............................")
print("Seja bem-vindo(a)!")

nome = input("Me diga, por favor,o seu nome:")
idade= int (input("Agora presciso que voce me informe a sua idade:"))
altura = float(input("informe a sua altura"))
nascimento = 2024 - idade 
peso = float (input("informe o seu peso"))
IMC = peso / (altura * altura)


print("Sua idade é: ", idade, "anos")
print("Sua altura é de: ", altura, "metros.")
print("Seu IMC é: {:.2f} kg/m²".format(IMC))