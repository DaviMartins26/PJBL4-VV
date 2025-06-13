import unittest
from TDD.funcoes import alterar_tipo_item, ITENS_FILE

class TestAlterarTipoItem(unittest.TestCase):
    def setUp(self):
        # Garante que, antes de cada teste, o item 109 exista como "achado"
        linhas = []
        with open(ITENS_FILE, "r", encoding="utf-8") as f:
            for linha in f:
                if linha.startswith("#"):
                    linhas.append(linha); continue
                partes = linha.strip().split(", ")
                if partes[0] == "109":
                    partes[5] = "achado"
                linhas.append(", ".join(partes) + "\n")
        with open(ITENS_FILE, "w", encoding="utf-8") as f:
            f.writelines(linhas)

    def test_alterar_tipo_item_109(self):
        # Executa a função
        sucesso = alterar_tipo_item(109, "devolvido")
        # Verifica o retorno booleano
        self.assertTrue(sucesso)
        # Verifica no arquivo se realmente mudou para "devolvido"
        with open(ITENS_FILE, "r", encoding="utf-8") as f:
            for linha in f:
                if linha.startswith("#"):
                    continue
                partes = linha.strip().split(", ")
                if partes[0] == "109":
                    self.assertEqual(partes[5], "devolvido")
                    break
            else:
                self.fail("Item 109 não foi encontrado em itens.txt")

if __name__ == "__main__":
    unittest.main()


# python -m unittest discover -s TDD -p "TDD_test9.py" -v