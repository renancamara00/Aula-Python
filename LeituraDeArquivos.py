arquivo = open("dados.txt", "r")  # Abrir o arquivo em modo de leitura
conteudo = arquivo.read()  # Ler o conteúdo do arquivo
print(conteudo)  # Exibir o conteúdo do arquivo
arquivo.close()  # Fechar o arquivo após a leitura

arquivo = open("dados.txt", "w")  # Abrir o arquivo em modo de gravação
arquivo.write("Teste de gravação\n")  # Escrever uma nova linha no arquivo
arquivo.close()  # Fechar o arquivo após a gravação

with open("dados.txt", "a") as arquivo:  # Abrir o arquivo em modo de anexação
    arquivo.write("Linha adicional\n")  # Escrever uma nova linha no final do arquivo
    print(conteudo)  # Exibir o conteúdo do arquivo dentro do bloco with