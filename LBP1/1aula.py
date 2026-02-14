#revisão básica

nome = input("Digite seu nome: ")
notas = list(map(int,input("Digite as notas para o cálculo da média: ").split()))
media = 0
for c in notas:
    media += c
media = media/len(notas)
print(f"Nome: {nome}\nmédia: {media}")
