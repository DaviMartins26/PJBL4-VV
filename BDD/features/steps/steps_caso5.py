from behave import given, when, then
from BDD.funcoes import cadastrar_item_achado

@given('o usuario informa os dados do item achado com id "{id}", nome "{nome}", item "{item}", data "{data}" e local "{local}"')
def step_given_dados_item(context, id, nome, item, data, local):
    context.id = int(id)
    context.nome = nome
    context.item = item
    context.data = data
    context.local = local

@when('envia a solicitacao de cadastro do item achado')
def step_when_envia_cadastro(context):
    context.resultado = cadastrar_item_achado(context.id, context.nome, context.item, context.data, context.local)

@then('o sistema registra o item no arquivo como tipo achado')
def step_then_verifica_registro(context):
    assert context.resultado == "Item achado registrado com sucesso"
    
    with open("itens.txt", "r", encoding="utf-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]
    
    achado_registrado = f"{context.id}, {context.nome}, {context.item}, {context.data}, {context.local}, achado"
    assert achado_registrado in linhas, "O item achado não foi registrado corretamente"
