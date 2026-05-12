temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
 ]

count = 0
anterior = 0
for linha in temperaturas:
    media = 0
    count += 1
    critico = 0
    for coluna in linha:
        media += coluna
        if coluna >= 33:
            critico += 1
    print(f"Sala {count}")
    print(f"Média: {media / len(linha) } ")
    print(f"Registros críticos: {critico}")

    if critico > anterior:
        posicao = count

    anterior = critico
print(f"Sala com maior risco: {posicao} ")



