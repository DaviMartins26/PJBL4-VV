from behave import given, when, then
from BDD.funcoes import alterar_tipo_item, BASE_DIR, ITENS_FILE
import os

@given('o arquivo de itens está carregado com o item {id_item:d} do tipo "{tipo}"')
def step_given_item_tipo(context, id_item, tipo):
    # força no arquivo o tipo inicial do item
    path = ITENS_FILE
    linhas = []
    with open(path, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.startswith("#"):
                linhas.append(linha); continue
            partes = linha.strip().split(", ")
            if partes[0] == str(id_item):
                partes[5] = tipo
            linhas.append(", ".join(partes) + "\n")
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(linhas)
    context.id_item = id_item

@when('eu altero o tipo do item com id "{id_item}" para "{novo_tipo}"')
def step_when_alterar(context, id_item, novo_tipo):
    context.sucesso = alterar_tipo_item(context.id_item, novo_tipo)

@then('a operação deve ser bem-sucedida')
def step_then_sucesso(context):
    assert context.sucesso is True

@then('o tipo do item com id "{id_item}" deve ser "{novo_tipo}"')
def step_then_verifica_tipo(context, id_item, novo_tipo):
    path = ITENS_FILE
    with open(path, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.startswith("#"):
                continue
            partes = linha.strip().split(", ")
            if partes[0] == str(context.id_item):
                assert partes[5] == novo_tipo
                return
    assert False, f"Item {context.id_item} não encontrado em {path}"


# . .\.venv\Scripts\Activate.ps1
# python -m behave --no-capture -v BDD/features/BDD_test9.feature