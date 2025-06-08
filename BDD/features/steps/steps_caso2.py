from behave import when, then
from BDD.funcoes import cadastrar_usuario

@when('cadastro o usuario "{nome}" com email "{email}" e senha "{senha}"')
def step_when_cadastrar_usuario(context, nome, email, senha):
    context.resposta = cadastrar_usuario(nome, email, senha)

@then('caso2-o sistema deve exibir "{mensagem}"')
def step_then_resultado_cadastro(context, mensagem):
    print("RESPOSTA OBTIDA:", context.resposta)
    assert context.resposta == mensagem

