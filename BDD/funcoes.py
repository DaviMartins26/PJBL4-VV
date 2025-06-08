#colocar Teste1,2...
#teste 1
def carregar_usuarios():
    usuarios = {}
    with open("user.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.startswith("#"): continue
            partes = [p.strip() for p in linha.strip().split(",")]
            if len(partes) < 5:
                continue  # ignora linhas incompletas
            id_, nome, email, senha, cargo = partes
            usuarios[email] = {
                "id": id_,
                "nome": nome,
                "senha": senha,
                "cargo": cargo
            }
    return usuarios
def login(nome, email, senha):
    usuarios = carregar_usuarios()
    if email in usuarios and usuarios[email]["senha"] == senha and usuarios[email]["nome"] == nome:
        return f"Bem-vindo {nome}"
    return "Login invalido"

#teste 2

def salvar_usuario(nome, email, senha, cargo="Usuario"):
    with open("user.txt", "r", encoding="utf-8") as arquivo:
        linhas = [l.strip() for l in arquivo if l.strip() and not l.startswith("#")]

    # Verifica se a linha tem um ID numérico no início
    ids = []
    for l in linhas:
        partes = [p.strip() for p in l.split(",")]
        if len(partes) >= 1:
            try:
                ids.append(int(partes[0]))
            except ValueError:
                continue  # ignora linhas mal formatadas

    ultimo_id = max(ids) if ids else 0
    novo_id = ultimo_id + 1

    with open("user.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{novo_id}, {nome}, {email}, {senha}, {cargo}\n")

def cadastrar_usuario(nome, email, senha, cargo="Usuario"):
    usuarios = carregar_usuarios()
    if email in usuarios:
        return "Erro: Email ja cadastrado"
    salvar_usuario(nome, email, senha, cargo)
    return "Usuario cadastrado com sucesso"



#Teste 7
def filtrar_por_data(data):
    resultados = []
    with open("itens.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.startswith("#"): continue
            partes = [p.strip() for p in linha.strip().split(",")]
            if len(partes) >= 4 and partes[3] == data:
                resultados.append(", ".join(partes))
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
            partes = [p.strip() for p in linha.strip().split(",")]
            if len(partes) >= 6 and partes[0].isdigit() and int(partes[0]) == id_item:
                partes[4] = novo_local
                sucesso = True
            linhas.append(", ".join(partes) + "\n")
    if sucesso:
        with open("itens.txt", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas)
    return sucesso
