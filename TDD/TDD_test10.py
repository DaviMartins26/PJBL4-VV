import unittest
from TDD.funcoes import alterar_senha_usuario, USER_FILE

class TestAlterarSenhaUsuario(unittest.TestCase):
    def setUp(self):
        # Garante estado inicial: senha "senhaAntiga!" para este email
        linhas = []
        with open(USER_FILE, "r", encoding="utf-8") as f:
            for linha in f:
                if linha.startswith("#"):
                    linhas.append(linha)
                    continue
                partes = [p.strip() for p in linha.strip().split(",")]
                if partes[2] == "daniel.lima@email.com":
                    partes[3] = "senhaAntiga!"
                linhas.append(", ".join(partes) + "\n")
        with open(USER_FILE, "w", encoding="utf-8") as f:
            f.writelines(linhas)

    def test_alterar_senha_daniel(self):
        # 1) chama a função
        sucesso = alterar_senha_usuario(
            "daniel.lima@email.com",
            "novaSenha123"
        )
        # 2) valida retorno
        self.assertTrue(sucesso)

        # 3) confirma no mesmo USER_FILE
        with open(USER_FILE, "r", encoding="utf-8") as f:
            for linha in f:
                if linha.startswith("#"):
                    continue
                partes = [p.strip() for p in linha.strip().split(",")]
                if partes[2] == "daniel.lima@email.com":
                    self.assertEqual(partes[3], "novaSenha123")
                    break
            else:
                self.fail("Usuário não encontrado em " + USER_FILE)

if __name__ == "__main__":
    unittest.main()

# python -m unittest TDD.TDD_test10 -v