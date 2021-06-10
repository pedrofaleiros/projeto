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

if conexao:
    print('deu certo')    

    for i in range(4500, 5000):
        nome = f'professor{i+1}'
        preco = 20+randint(1, 100)
        materia = materias[randint(0, len(materias)-1)]
        contato = f'9999-{i+1}'
        obs = f'observacoes {nome}'
        cc.execute(f'insert into professor(nome, preco, materia, contato, obs) values("{nome}", {preco}, "{materia}", "{contato}", "{obs}");')


    cc.close()
    conexao.close()
    