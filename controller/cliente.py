#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(curso, matrícula, nome, endereço, idade):
    db.cur.execute("""
                   INSERT into tb_aluno (curso, matrícula, nome, endereço, idade)
                   VALUES ('%s','%s','%s','%s','%s')
                   """ % (curso, matrícula, nome, endereço, idade ))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM tb_aluno
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def excluir(nome):
    db.cur.execute("""
                   DELETE FROM tb_aluno WHERE nome = '%s'
                   """ % (nome))
    db.con.commit()

def atualizar(matrícula):
    db.cur.execute("""
                   UPDATE FROM tb_aluno WHERE matrícula = '%s'
                   """ % (matrícula))
    db.con.commit()


