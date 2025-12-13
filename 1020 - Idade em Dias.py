tempo = int(input())
ano = tempo//365
tempo %= 365
mes = tempo//30
dia = tempo % 30
print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')