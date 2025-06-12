from behave import given, when, then
from BDD.funcoes import listar_itens_achados
import io
import sys

@given("que o arquivo de itens já existe e contém registros")
def step_given_arquivo_existe(context):
    # Assume que o arquivo itens.txt já existe com conteúdo adequado
    pass  # Nenhuma ação é necessária

@when("o usuario solicita listar os itens do tipo achado")
def step_when_listar_achados(context):
    # Redireciona a saída padrão para capturar o print da função
    context.stdout_backup = sys.stdout
    sys.stdout = context.captura = io.StringIO()
    listar_itens_achados()
    sys.stdout = context.stdout_backup

@then("o sistema exibe apenas os itens marcados como achado")
def step_then_verifica_listagem(context):
    saida = context.captura.getvalue()
    linhas = saida.strip().split("\n")

    for linha in linhas:
        assert linha.strip().endswith("achado"), f"Linha inválida: {linha}"
