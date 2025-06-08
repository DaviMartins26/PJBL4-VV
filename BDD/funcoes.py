#colocar Teste1,2...


#Teste 7
def filtrar_por_data(data):
    resultados = []
    with open("itens.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.startswith("#"): continue
            partes = linha.strip().split(", ")
            if partes[3] == data:
                resultados.append(linha.strip())
    return resultados

#Teste 8
def alterar_local(id_item, novo_local):
    linhas = []
    sucesso = False
    with open("itens.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.startswith("#"):
                linhas.append(linha)
                continue
            partes = linha.strip().split(", ")
            if int(partes[0]) == id_item:
                partes[4] = novo_local
                sucesso = True
                linha = ", ".join(partes)
            linhas.append(linha + "\n")
    if sucesso:
        with open("itens.txt", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas)
    return sucesso