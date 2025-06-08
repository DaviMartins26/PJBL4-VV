from behave import given, when, then
from BDD.funcoes import filtrar_por_data

@given('o usuario informa a data "{data}"')
def step_given_data(context, data):
    context.data = data

@when('envia a solicitacao de filtro')
def step_when_enviar_filtro(context):
    context.resultado = filtrar_por_data(context.data)

@then('o sistema retorna todos os itens com a data "{data}"')
def step_then_resultado_filtrado(context, data):
    for item in context.resultado:
        assert data in item, f"Item '{item}' nao possui a data '{data}'"
