cnt = 1

while True:
    N, M = map(int, input().split())
    
    if N == M == 0:
        break
    
    temperaturas = [int(input()) for j in range(N)]
        
    soma_atual = sum(temperaturas[0:M])
    
    media_atual = soma_atual // M
    menor_media = media_atual
    maior_media = media_atual
    
    for i in range(1, N - M + 1):
        elemento_saiu = temperaturas[i-1]
        elemento_entrou = temperaturas[i + M - 1]
        soma_atual = soma_atual + elemento_entrou - elemento_saiu
        
        media_atual = int(soma_atual / M)
        
        if media_atual < menor_media:
            menor_media = media_atual
        elif media_atual > maior_media:
            maior_media = media_atual
    
    print(f"Teste {cnt}")  
    print(menor_media, maior_media)
    print()
    cnt+=1