print("-" * 40)

nome = input("Digite uma palavra: ").upper()
print(nome, nome[::-1])

if nome == nome[::-1]:
    print("O texto digitado \033[34mé um Palindromo.\33[m")
else:
    print("O texto digitado \33[31mnão é um Palindromo.\33[m")

print("-" * 40)

