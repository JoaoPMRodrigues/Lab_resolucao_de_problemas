hora_inicial, minuto_inicial, hora_final, minuto_final = map(
    int, input().split())
tempo_inicial = hora_inicial * 60 + minuto_inicial
tempo_final = hora_final * 0 + minuto_final

if tempo_inicial == tempo_final:
    horas = 24
    minutos = 0
elif tempo_inicial < tempo_final:
    tempo_jogo = tempo_final - tempo_inicial
    horas = tempo_jogo//60
    minutos = tempo_jogo % 60
else:
    tempo_jogo = 1440 - tempo_inicial + tempo_final
    horas = tempo_jogo // 60
    minutos = tempo_jogo % 60
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
