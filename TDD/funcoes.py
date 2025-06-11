#colocar Teste1,2...
# Teste 1
def carregar_usuarios():
    usuarios = {}
    try:
        with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.strip():
                    nome, email, senha = linha.strip().split(", ")
                    usuarios[email] = {"nome": nome, "senha": senha}
    except FileNotFoundError:
        pass
    return usuarios

def login(nome, email, senha):
    usuarios = carregar_usuarios()
    if email in usuarios and usuarios[email]["senha"] == senha and usuarios[email]["nome"] == nome:
        return f"Bem-vindo {nome}"
    return "Login invalido"

# Teste 2
def salvar_usuario(nome, email, senha):
    with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}, {email}, {senha}\n")

def cadastrar_usuario(nome, email, senha):
    usuarios = carregar_usuarios()
    if email in usuarios:
        return "Erro: Email ja cadastrado"
    salvar_usuario(nome, email, senha)
    return "Usuario cadastrado com sucesso"
    

# Teste 3
def cadastrar_item_perdido(id, nome, descricao, data, local, status):
    with open("itens_perdidos.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{id}, {nome}, {descricao}, {data}, {local}, {status}\n"
        arquivo.write(linha)
    return "Cadastro realizado com sucesso"

# Teste 4
def filtrar_itens_perdidos(itens, filtro):
    return [item for item in itens
            if item.get("local") == filtro.get("local") and item.get("status") == filtro.get("status")]
    
# Teste 5
def cadastrar_item_achado(id, nome_registrador, item, data, local):
    tipo = "achado"
    with open("itens.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{id}, {nome_registrador}, {item}, {data}, {local}, {tipo}\n"
        arquivo.write(linha)
    return "Item achado registrado com sucesso"

# Teste 6
def listar_itens_achados():
    try:
        with open("itens.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.strip().endswith("achado"):
                    print(linha.strip())
    except FileNotFoundError:
        print("Arquivo 'itens.txt' não encontrado.")


# Teste 7
def filtrar_por_data(data):
    resultados = []
    with open("itens.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.startswith("#"): continue
            partes = linha.strip().split(", ")
            if partes[3] == data:
                resultados.append(linha.strip())
    return resultados

# Teste 8
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
