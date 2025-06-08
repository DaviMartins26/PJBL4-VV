Feature: Login de Usuario

  Scenario: Login bem-sucedido
    Given o usuario "Ana Silva" com email "ana.silva@email.com" e senha "senha123" esta cadastrado
    When ele tenta fazer login com nome "Ana Silva", email "ana.silva@email.com" e senha "senha123"
    Then caso1-o sistema deve exibir "Bem-vindo Ana Silva"
