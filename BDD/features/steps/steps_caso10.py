from behave import given, when, then
from BDD.funcoes import alterar_senha_usuario, USER_FILE

@given('o arquivo de usuários está carregado com o usuário "{email}" com senha "{senha}"')
def step_given_usuario_com_senha(context, email, senha):
    # força o estado inicial para sempre começar de senhaAntiga!
    linhas = []
    with open(USER_FILE, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.startswith("#"):
                linhas.append(linha); continue
            partes = [p.strip() for p in linha.strip().split(",")]
            if partes[2] == email:
                partes[3] = senha
            linhas.append(", ".join(partes) + "\n")
    with open(USER_FILE, "w", encoding="utf-8") as f:
        f.writelines(linhas)
    context.email = email

@when('eu altero a senha para "{nova_senha}"')
def step_when_alterar_senha(context, nova_senha):
    context.sucesso = alterar_senha_usuario(context.email, nova_senha)
    context.nova_senha = nova_senha

@then('a operação deve ser bem‐sucedida')
def step_then_sucesso(context):
    assert context.sucesso is True

@then('o usuário com email "{email}" deve ter a senha "{senha}"')
def step_then_verifica_senha(context, email, senha):
    # lê de volta do mesmo USER_FILE
    with open(USER_FILE, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.startswith("#"):
                continue
            partes = [p.strip() for p in linha.strip().split(",")]
            if partes[2] == email:
                assert partes[3] == senha
                return
    assert False, f"Usuário {email} não encontrado em {USER_FILE}"

# . .\.venv\Scripts\Activate.ps1
# python -m behave --no-capture -v BDD/features/BDD_test10.feature
