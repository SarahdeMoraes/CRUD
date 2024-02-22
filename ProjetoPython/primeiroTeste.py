from pymongo import MongoClient

#conexão com o MongoDB
conexao=MongoClient("mongodb://localhost:27017")
#Criar um banco de dados
mongoDB1= conexao["mangoBD1" ]#<- O nome do banco no MONGODB vai ser chave
#Criar uma collection
collection_alunos = mongoDB1["alunos"] #<- O nome da collection no MONGODB vai ser chave

aluno1 = {
  "nome":"Marcelo",
  "sobrenome":"Grilo",
  "idade":35,
  "media":7.1
}
# (C) - Criando um documento
collection_alunos.insert_one(aluno1)

# (R) - Ler um documento
documentos=(collection_alunos.find()) # <- Um cursor é uma estrutura de dados que precisa ser "varrida"
for doc in documentos:
  for chave in doc:
    print(chave,':',doc[chave])

# (U) - Atualizar um documento
filtro={"nome":"Marcelo"}
resultado_update=collection_alunos.update_one(filter,{"$set":{"media":7.8}})
if resultado_update.modified_count>0:
  print('Ducumento foi atualizado')
else:
  print('Nada foi atualizado')








# (D) - Deletar um documento 
resultado_delete = collection_alunos.delete_one({"nome":"Marcelo"})
if resultado_delete.deleted_count>0:
   print('Documento foi deletado')
else:
   print('Seu banco não foi alterado')