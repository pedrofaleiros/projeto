from fastapi import FastAPI
import pymysql.cursors
from fastapi.responses import JSONResponse
from AMP.modelos.professor import ProfessorCadastro
from fastapi.middleware.cors import CORSMiddleware

#conectar banco de dados e fazer get e post
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

def abre_conexao(nome_db):
    conexao = pymysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
    #muda aqui
        db = nome_db,
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )
    return conexao

def fecha_conexao(conexao, cursor):
    cursor.close()
    conexao.close()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/professor')
async def recupera_prof():
    conexao = abre_conexao('projetoamp')
    cursor = conexao.cursor()

    cursor.execute("select * from professor;")
    dados = cursor.fetchall()
    #algoritmo aqui
    #passava tempo de execucao tbm
    fecha_conexao(conexao, cursor)

    quicksort(dados, 0, len(dados)-1)

    return {"resposta":dados}

@app.post('/professor', status_code=201)
async def cadastra_prof(professor:ProfessorCadastro):
    conexao = abre_conexao('projetoamp')
    cursor = conexao.cursor()
    valor = professor.preco

    query = f'insert into professor(nome, preco, materia, contato, obs) values("{professor.nome}", {professor.preco}, "{professor.materia}", "{professor.contato}", "{professor.obs}");'

    cursor.execute(query)
    id_retorno = cursor.lastrowid
    fecha_conexao(conexao, cursor)

    return {'id_cadastrado':id_retorno}
