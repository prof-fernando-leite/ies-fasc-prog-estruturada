import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="db"
)

cursor = conexao.cursor()
print("Conexão estabelecida!")

# cursor.execute('''
# insert into professor (nome, matricula) values ("Beltrano", "85839352");
# ''')
# conexao.commit()
# cursor.execute('''
# select * from professor;
#                ''')
# result = cursor.fetchall()
# print(type(result))
# print(type(result[0]))
# print("-------------------------------------")
# print(result)

cursor.execute('''
select nome, matricula from professor where matricula="300";
               ''')
result = cursor.fetchone()
print(type(result))
print("-------------------------------------")
print(result)


cursor.execute('''
select matricula, nome from professor where matricula="300";
               ''')
result = cursor.fetchone()
print(type(result))
print("-------------------------------------")
print(result)
cursor.close()
conexao.close()
print("Dados salvos com sucesso!")