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
                print("BURRO")
    return resultados
