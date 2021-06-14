
function mostra_na_tela(dados, num_cadastros){
    
    let pessoas = document.getElementById('pessoas')

    pessoas.innerHTML = ' '
    
    for(let i = 0; i < num_cadastros; i += 1){
        let item = document.createElement('li')
        let nome = document.createElement('p')
        let preco = document.createElement('h3')

        nome.innerHTML = `${dados[i]['nome']}`
        preco.innerHTML = `Preço: R$${dados[i]['preco']}`
        
        item.appendChild(nome)
        
        item.innerHTML = item.innerHTML + `${dados[i]['materia']} - Contato: ${dados[i]['contato']}`
        item.appendChild(preco)
        
        pessoas.appendChild(item)
    }
}

function mostrar_dados(algoritmo, filtro){

    let url = `http://localhost:8000/prof_${algoritmo}_${filtro}`

    fetch(url)
    .then(function(response){
        return response.json();
    })
    .then(function(data){

    var dados = data['resposta']
    let tempo = data['tempo']
    let n_cad = data['numero']

    let texto_tempo = document.getElementById('tempo')
    let num_cadastros = document.getElementById('total')

    mostra_na_tela(dados, n_cad)

    texto_tempo.innerText = tempo + ' segundos para ordenar'
    num_cadastros.innerText = n_cad + ' cadastros'

    });


}

function quicksort(){

    let check = document.getElementsByName('nome')
    let check2 = document.getElementsByName('preco')
    
    if(check[0].checked == true){
        
        if(check2[0].checked == true){
            alert('Escolha apenas um filtro')
        }else{
            mostrar_dados('quick', 'nome')
        }
    }else{
        if(check2[0].checked == true){
            mostrar_dados('quick', 'preco')
        }else{
            alert('Escolha um Filtro')
        }
    }
    
    
}

function bubblesort(){
    
    let check = document.getElementsByName('nome')
    let check2 = document.getElementsByName('preco')
    
    if(check[0].checked == true){
        if(check2[0].checked == true){
            alert('Escolha apenas um filtro')
        }else{
            mostrar_dados('bubble', 'nome')
        }
    }else{
        if(check2[0].checked == true){
            mostrar_dados('bubble', 'preco')
        }else{
            alert('Escolha um Filtro')
        }
    }
}
