A = str(input("Digite uma frase: ")).strip().upper()
print("A quantidade de 'A' que aparece é : {} ".format(A.count("A")))
print("A primeira letra A apareceu na posição {}".format(A.find("A")+1))
print("A última letra A apareceu na posição {}".format(A.rfind("A")+1))