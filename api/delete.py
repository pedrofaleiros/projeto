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

    for i in range(800, 987):
        nome = 'professor'+str(i)
        cc.execute(f'delete from professor where nome="{nome}"')
        print(i)
    cc.close()
    conexao.close()

