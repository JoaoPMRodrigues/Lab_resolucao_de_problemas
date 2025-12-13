import sys
import math

def main():
    dados = sys.stdin.read().strip().split()
    i = 0
    ctd = 1
    saida = []

    while True:
        if i >= len(dados):
            break

        n = int(dados[i])
        i += 1
        if n == 0:
            break

        cidade = {}
        total_pessoas = 0
        total_consumo = 0

        for _ in range(n):
            x = int(dados[i])
            y = int(dados[i + 1])
            i += 2

            media = y // x  
            total_pessoas += x
            total_consumo += y

            if media not in cidade:
                cidade[media] = 0
            cidade[media] += x

        ordenado = sorted(cidade.items())

        saida.append(f"Cidade# {ctd}:")
        saida.append(' '.join(f"{p}-{m}" for m, p in ordenado))

        media_total = math.floor((total_consumo / total_pessoas) * 100) / 100
        saida.append(f"Consumo medio: {media_total:.2f} m3.\n")

        ctd += 1

    print('\n'.join(saida).strip())

if __name__ == "__main__":
    main()