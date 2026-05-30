pessoa = {"nome": "Alice", "idade": 30, "cidade": "Sao Paulo"}

print(pessoa["nome"])  # Acessando o valor associado à chave "nome"
print(pessoa["idade"])  # Acessando o valor associado à chave "idade"   
print(pessoa["cidade"])  # Acessando o valor associado à chave "cidade"
pessoa["profissao"] = "Engenheira"  # Adicionando um novo par chave-valor

print(pessoa.get("nome"))  # Acessando o valor associado à chave "nome" usando o método get()

print(pessoa.keys())  # Imprimindo todas as chaves do dicionário
print(pessoa.values())  # Imprimindo todos os valores do dicionário
print(pessoa.items())  # Imprimindo todos os pares chave-valor do dicionário   

pessoa.update({"Escolaridade": "Ensino Superior"})  # Atualizando o dicionário com um novo par chave-valor  
print(pessoa)