from behave import given, when, then
from BDD.funcoes import cadastrar_usuario, login

@given('o usuario "{nome}" com email "{email}" e senha "{senha}" esta cadastrado')
def step_given_usuario_cadastrado(context, nome, email, senha):
    cadastrar_usuario(nome, email, senha)

@when('ele tenta fazer login com nome "{nome}", email "{email}" e senha "{senha}"')
def step_when_tenta_login(context, nome, email, senha):
    context.resultado = login(nome, email, senha)

@then('caso1-o sistema deve exibir "{mensagem}"')
def step_then_resultado_login(context, mensagem):
    assert context.resultado == mensagem
