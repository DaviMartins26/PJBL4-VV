Feature: Cadastro de Usuario

  Scenario: Cadastro com sucesso
    When cadastro o usuario "Joana" com email "joana@email.com" e senha "abcd"
    Then caso2-o sistema deve exibir "Usuario cadastrado com sucesso"
