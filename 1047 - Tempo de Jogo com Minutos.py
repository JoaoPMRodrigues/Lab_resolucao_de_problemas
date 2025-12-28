hora_inicial, minuto_inicial, hora_final, minuto_final = map(
    int, input().split())
if hora_inicial == hora_final and minuto_inicial == minuto_final:
    horas = 24
    minutos = 0
elif hora_inicial < hora_final and minuto_inicial > minuto_final:
    horas = hora_final - (hora_inicial + 1)
    minutos = minuto_inicial + minuto_final - 60
elif hora_inicial < hora_final and minuto_inicial < minuto_final:
    horas = hora_final - hora_inicial
    minutos = minuto_inicial - minuto_final

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
