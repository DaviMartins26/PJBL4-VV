from behave import given, when, then
from BDD.funcoes import alterar_local

@given('o usuario informa o ID "{id_item}" e o novo local "{novo_local}"')
def step_given_id_local(context, id_item, novo_local):
    context.id_item = int(id_item)  # <- conversão de sting pra int
    context.novo_local = novo_local

@when('envia a solicitacao de atualizacao')
def step_when_envia_atualizacao(context):
    context.resultado = alterar_local(context.id_item, context.novo_local)

@then('o sistema atualiza o local do item no arquivo')
def step_then_local_atualizado(context):
    assert context.resultado == True, "O local do item nao foi atualizado com sucesso"
