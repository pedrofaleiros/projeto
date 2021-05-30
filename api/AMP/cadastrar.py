import pymysql.cursors
from random import randint

conexao = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    db = 'projetoamp',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cc = conexao.cursor()

materias = ['portugues', 'matematica', 'biologia', 'historia', 'geografia', 'artes', 'fisica', 'literatura', 'ciencias', 'quimica']
precos = [1.99, 2, 2.99, 3, 4.99, 5.99, 6.99, 9.99, 10, 12, 14, 15, 16, 19, 20, 19.99, 25, 24.99, 5, 29.99, 30, 27.99, 28, 29, 33, 33.99, 34.99, 39.99, 40, 50, 49.99, 45, 44.99, 43, 42, 23, 17, 7, 6]

if conexao:
    print('deu certo')    

    for i in range(100,500):
        nome = f'professor{i+1}'
        preco = precos[randint(0, len(precos)-1)]
        materia = materias[randint(0, len(materias)-1)]
        contato = f'9999-{i+1}'
        obs = f'observacoes {nome}'
        # cc.execute(f'insert into professor(nome, preco, materia, contato, obs) values("{nome}", {preco}, "{materia}", "{contato}", "{obs}");')


    cc.close()
    conexao.close()
    