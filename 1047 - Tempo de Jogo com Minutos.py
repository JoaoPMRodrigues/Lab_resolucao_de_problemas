hora_inicial, minuto_inicial, hora_final, minuto_final = map(
    int, input().split())
# Horas iguais
if hora_inicial == hora_final and minuto_inicial == minuto_final:
    horas = 24
    minutos = 0
elif hora_inicial == hora_final and minuto_inicial > minuto_final:
    horas = 23
    minutos = 60 - minuto_inicial + minuto_final
elif hora_inicial == hora_final and minuto_inicial < minuto_final:
    horas = 0
    minutos = minuto_final - minuto_inicial
# Hora inicial < hora final
elif hora_inicial < hora_final and minuto_inicial == minuto_final:
    horas = hora_final - hora_inicial
    minutos = 0
elif hora_inicial < hora_final and minuto_inicial < minuto_final:
    horas = hora_final - hora_inicial
    minutos = minuto_inicial - minuto_final
elif hora_inicial < hora_final and minuto_inicial > minuto_final:
    horas = hora_final - (hora_inicial + 1)
    minutos = 60 - minuto_inicial + minuto_final
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
