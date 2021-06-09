def quicksort(pessoas, inicio, final, filtro='preco'):

    if inicio >= final:
        return

    i = inicio
    pivo = pessoas[i][filtro]
    j = final

    while j != i:
        if i > j:
            if pessoas[j][filtro] > pivo:
                pessoas[i], pessoas[j] = pessoas[j], pessoas[i]
                i, j = j, i
                
        else:
            if pessoas[j][filtro] < pivo:
                pessoas[i], pessoas[j] = pessoas[j], pessoas[i]
                i, j = j, i

        if i > j:
            j += 1
        else:
            j -= 1
    
    quicksort(pessoas, inicio, i-1, filtro)
    quicksort(pessoas, i+1, final, filtro)

def bubblesort(pessoas, tamanho, filtro='preco'):
    trocou = True
    i = 0
    while i < tamanho-1 and trocou:
        trocou = False
        j = 0
        while j < tamanho-1-i:
            if pessoas[j][filtro] > pessoas[j+1][filtro]:
                trocou = True

                pessoas[j], pessoas[j+1] = pessoas[j+1], pessoas[j]

            j += 1
        i += 1
