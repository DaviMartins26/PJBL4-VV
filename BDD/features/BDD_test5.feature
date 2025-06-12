Feature: Registrar item achado
  Como um funcionario do sistema
  Quero cadastrar um item que foi encontrado
  Para que ele possa ser identificado e devolvido ao dono

  Scenario: Registrar um novo item achado
    Given o usuario informa os dados do item achado com id "201", nome "Joshua", item "Caderno Preto", data "10/06/2025" e local "Sala 101"
    When envia a solicitacao de cadastro do item achado
    Then o sistema registra o item no arquivo como tipo achado
