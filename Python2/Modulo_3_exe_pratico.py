"""
1.	Crie uma base de dados chamada sistema_escolar_soul_on
2.	Crie uma tabela alunos com os campos id, nome, matricula, turma.
3.	Alimente a tabela com os seguintes dados:
"""
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "sistema_escolar_soul_on"
)

mycursor = db.cursor()
#mycursor.execute("CREATE DATABASE sistema_escolar_soul_on")
#print("Database criada com sucesso!")

#mycursor.execute("CREATE TABLE alunos(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), matricula VARCHAR(255), turma VARCHAR(255))")
#print("Tabela criada com sucesso!")

#adicionar = "INSERT INTO alunos (name, matricula, turma) VALUES(%s, %s, %s)"
#val = [
#    ("José Lima", "MAT90551", "BCW22"),
#    ("Carlos Augusto", "MAT90552", "BCW22"),
#    ("Lívia Lima", "MAT90553", "BCW22"),
#    ("Sandra Gomes", "MAT90554", "BCW23"),
#    ("João Augusto", "MAT90555", "BCW23"),
#    ("Breno Lima", "MAT90556", "BCW24"),
#    ("José Vinícius", "MAT90557", "BCW25")
#]
#mycursor.executemany(adicionar,  val)
#print(mycursor.rowcount, "linha(s) alterada(s)!")
#db.commit()

"""4.	Faça as seguintes consultas:
•	Liste todos os registros de sua tabela.
•	Liste apenas nome e matrícula dos alunos do BCW23.
•	Liste apenas o nome dos alunos que tiverem o sobrenome Lima.
"""
#mycursor.execute("SELECT * FROM alunos")
#mycursor.execute("SELECT name FROM alunos WHERE turma = 'BCW23' ")
#adicionar = "SELECT name FROM alunos WHERE name LIKE '%Lima%'"
#mycursor.execute(adicionar)

#myresult = mycursor.fetchall()
#for x in myresult:
#    print(x)

'''
5.	O aluno Carlos Augusto está na turma errada. Matricule o mesmo no BCW25.
6.	O aluno José Vinicius desistiu do curso, ele deve ser excluído do sistema.
'''

#adicionar = "UPDATE alunos SET turma = 'BCW25' WHERE  name = 'Carlos Augusto'"
adicionar = "DELETE FROM alunos WHERE  name = 'José Vinicius'"
mycursor.execute(adicionar)
#db.commit()
print(mycursor.rowcount, "Linha(s) afetada(s)")
