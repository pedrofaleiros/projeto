import pymysql.cursors

conexao = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    db = 'projetoamp',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cc = conexao.cursor()

if conexao:
    print('deu certo')    
    cc.execute("""select * from professor;""")
    dados = cc.fetchall()
    cc.close()
    conexao.close()

for dado in dados:
    print(dado['nome'], end=' - ')
    print(dado['contato'])


