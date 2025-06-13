#colocar Teste1,2...
# Teste 1
def carregar_usuarios():
    usuarios = {}
    try:
        with open("user.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.strip() and not linha.startswith("#"):
                    partes = [parte.strip() for parte in linha.strip().split(",")]
                    if len(partes) >= 4:  # Pula se não tiver ao menos Nome, Email, Senha
                        nome = partes[1]
                        email = partes[2]
                        senha = partes[3]
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
    with open("user.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}, {email}, {senha}\n")

def cadastrar_usuario(nome, email, senha):
    usuarios = carregar_usuarios()
    if email in usuarios:
        return "Erro: Email ja cadastrado"
    salvar_usuario(nome, email, senha)
    return "Usuario cadastrado com sucesso"
    

# Teste 3
def cadastrar_item_perdido(id, nome, descricao, data, local, status):
    with open("itens.txt", "a", encoding="utf-8") as arquivo:
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
            if linha.startswith("#") or linha.strip() == "":
                continue
            partes = linha.strip().split(", ")
            if len(partes) >= 6 and partes[3] == data:
                resultados.append(linha.strip())
    return resultados


# Teste 8
def alterar_local(id_item, novo_local):
    linhas = []
    sucesso = False
    with open("itens.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.startswith("#") or linha.strip() == "":
                linhas.append(linha)
                continue
            partes = linha.strip().split(", ")
            if len(partes) >= 6 and int(partes[0]) == id_item:
                partes[4] = novo_local
                sucesso = True
                linha = ", ".join(partes)
            linhas.append(linha + "\n")
    if sucesso:
        with open("itens.txt", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas)
    return sucesso

# Teste 9
import os

BASE_DIR   = os.path.dirname(__file__)
ITENS_FILE = os.path.join(BASE_DIR, "itens.txt")

def alterar_tipo_item(id_item, novo_tipo):
    sucesso = False
    linhas   = []
    with open(ITENS_FILE, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.startswith("#"):
                linhas.append(linha); continue
            partes = linha.strip().split(", ")
            if partes[0] == str(id_item):
                partes[5] = novo_tipo
                sucesso   = True
            linhas.append(", ".join(partes) + "\n")
    if sucesso:
        with open(ITENS_FILE, "w", encoding="utf-8") as f:
            f.writelines(linhas)
    return sucesso

# Teste 10
import os

BASE_DIR  = os.path.dirname(__file__)
USER_FILE = os.path.join(BASE_DIR, "user.txt")

def alterar_senha_usuario(email, nova_senha):
    """
    Altera a senha do usuário com o email dado em TDD/user.txt.
    Retorna True se achou+alterou; False caso contrário.
    """
    sucesso = False
    linhas  = []

    # 1) lê o arquivo correto
    with open(USER_FILE, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.startswith("#"):
                linhas.append(linha)
                continue
            # separa por vírgula, limpa espaços
            partes = [p.strip() for p in linha.strip().split(",")]
            if len(partes) >= 4 and partes[2] == email:
                partes[3] = nova_senha
                sucesso   = True
            linhas.append(", ".join(partes) + "\n")

    # 2) sobrescreve apenas se realmente alterou
    if sucesso:
        with open(USER_FILE, "w", encoding="utf-8") as f:
            f.writelines(linhas)

    return sucesso

