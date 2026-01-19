yes = []
no = []
inscritos = [] 
while True:
    entrada = input().strip()
    if entrada == "FIM":
        break
    nome, opcao = entrada.split()
    inscritos.append((nome, opcao))  
    if opcao == "YES":
        yes.append(nome)
    else:
        no.append(nome)
yes_unicos = []
vistos = set()
for nome in yes:
    if nome not in vistos:
        vistos.add(nome)
        yes_unicos.append(nome)
yes_ordenados = sorted(yes_unicos)
no_ordenados = sorted(no)
for nome in yes_ordenados:
    print(nome)
for nome in no_ordenados:
    print(nome)
print()
print("Amigo do Habay:")
melhor_nome = ""
melhor_tamanho = -1
for nome, opcao in inscritos:
    if opcao == "YES":
        if len(nome) > melhor_tamanho:
            melhor_tamanho = len(nome)
            melhor_nome = nome

print(melhor_nome)