def quicksort(pessoas, inicio, final):

    if inicio >= final:
        return

    i = inicio
    pivo = pessoas[i]['preco']
    j = final

    while j != i:
        if i > j:
            if pessoas[j]['preco'] > pivo:
                aux = pessoas[i]['nome']
                pessoas[i]['nome'] = pessoas[j]['nome']
                pessoas[j]['nome'] = aux

                aux = pessoas[i]['preco']
                pessoas[i]['preco'] = pessoas[j]['preco']
                pessoas[j]['preco'] = aux

                aux = pessoas[i]['materia']
                pessoas[i]['materia'] = pessoas[j]['materia']
                pessoas[j]['materia'] = aux

                aux = pessoas[i]['contato']
                pessoas[i]['contato'] = pessoas[j]['contato']
                pessoas[j]['contato'] = aux
                
                aux = pessoas[i]['obs']
                pessoas[i]['obs'] = pessoas[j]['obs']
                pessoas[j]['obs'] = aux
                
                i, j = j, i

        else:
            if pessoas[j]['preco'] < pivo:
                aux = pessoas[i]['nome']
                pessoas[i]['nome'] = pessoas[j]['nome']
                pessoas[j]['nome'] = aux

                aux = pessoas[i]['preco']
                pessoas[i]['preco'] = pessoas[j]['preco']
                pessoas[j]['preco'] = aux

                aux = pessoas[i]['materia']
                pessoas[i]['materia'] = pessoas[j]['materia']
                pessoas[j]['materia'] = aux

                aux = pessoas[i]['contato']
                pessoas[i]['contato'] = pessoas[j]['contato']
                pessoas[j]['contato'] = aux
                
                aux = pessoas[i]['obs']
                pessoas[i]['obs'] = pessoas[j]['obs']
                pessoas[j]['obs'] = aux

                i, j = j, i

        if i > j:
            j += 1
        else:
            j -= 1
    
    quicksort(pessoas, inicio, i-1)
    quicksort(pessoas, i+1, final)

def bubblesort(pessoas, tamanho):
    trocou = True
    i = 0
    while i < tamanho-1 and trocou:
        trocou = False
        j = 0
        while j < tamanho-1-i:
            if pessoas[j]['preco'] > pessoas[j+1]['preco']:
                trocou = True

                aux = pessoas[j+1]['nome']
                pessoas[j+1]['nome'] = pessoas[j]['nome']
                pessoas[j]['nome'] = aux

                aux = pessoas[j+1]['preco']
                pessoas[j+1]['preco'] = pessoas[j]['preco']
                pessoas[j]['preco'] = aux

                aux = pessoas[j+1]['materia']
                pessoas[j+1]['materia'] = pessoas[j]['materia']
                pessoas[j]['materia'] = aux
                
                aux = pessoas[j+1]['contato']
                pessoas[j+1]['contato'] = pessoas[j]['contato']
                pessoas[j]['contato'] = aux
                
                aux = pessoas[j+1]['obs']
                pessoas[j+1]['obs'] = pessoas[j]['obs']
                pessoas[j]['obs'] = aux
            j += 1
        i += 1
