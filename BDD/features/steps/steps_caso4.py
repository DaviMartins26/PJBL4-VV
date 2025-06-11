from behave import given, when, then
from funcoes import filtrar_itens_perdidos

@given('que existem os seguintes itens perdidos cadastrados')
def step_dados_cadastrados(context):
    # Converte a tabela do feature em lista de dicionários
    context.itens = []
    for row in context.table:
        item = {
            "id": row['id'],
            "nome": row['nome'],
            "descricao": row['descricao'],
            "data": row['data'],
            "local": row['local'],
            "status": row['status']
        }
        context.itens.append(item)

@when('eu filtro os itens pelo local "{local}" e status "{status}"')
def step_filtrar_itens(context, local, status):
    filtro = {"local": local, "status": status}
    context.resultado = filtrar_itens_perdidos(context.itens, filtro)

@then('devo receber somente os itens que correspondem ao filtro')
def step_verificar_resultado(context):
    esperado = []
    for row in context.table:
        item = {
            "id": row['id'],
            "nome": row['nome'],
            "descricao": row['descricao'],
            "data": row['data'],
            "local": row['local'],
            "status": row['status']
        }
        esperado.append(item)
    assert context.resultado == esperado, f"Resultado: {context.resultado}, Esperado: {esperado}"
