hora_inicial, minuto_inicial, hora_final, minuto_final = map(
    int, input().split())
if hora_inicial == hora_final:
    horas = 24
elif hora_inicial < hora_final:
    horas = hora_final - hora_inicial
else:
    horas = hora_inicial + hora_final - 24
if minuto_inicial == minuto_final:
    minutos = 0
elif minuto_inicial < minuto_final:
    minutos = minuto_final - minuto_inicial
else:
    minutos = minuto_inicial + minuto_final - 60
    horas += 1

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
