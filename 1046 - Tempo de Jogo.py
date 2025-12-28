hora_inicial, hora_final = map(int, input().split())

if hora_inicial == hora_final:
    horas = 24
elif hora_inicial < hora_final:
    horas = hora_final - hora_inicial
else:
    horas = 24 - hora_inicial + hora_final

print(f"O JOGO DUROU {horas} HORA(S)")
