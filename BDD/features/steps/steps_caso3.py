import sys
import os

# Ajuste para importar o módulo funcoes corretamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from funcoes import cadastrar_item_perdido
from behave import given, when, then

@given('o sistema está pronto para cadastrar itens perdidos')
def step_sistema_pronto(context):
    pass  # Pode implementar preparação do ambiente aqui, se quiser

@when('cadastro um item com id "{id}", nome "{nome}", descrição "{descricao}", data "{data}", local "{local}" e status "{status}"')
def step_cadastrar_item(context, id, nome, descricao, data, local, status):
    context.resposta = cadastrar_item_perdido(id, nome, descricao, data, local, status)

@then('o sistema deve confirmar que o cadastro foi realizado com sucesso')
def step_verificar_cadastro(context):
    assert context.resposta == "Cadastro realizado com sucesso"