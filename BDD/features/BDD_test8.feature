Feature: Alterar local de um item
  Como usuario do sistema
  Quero atualizar o local de um item especifico
  Para manter as informacoes corretas

  Scenario: Alterar local do item com ID 109
    Given o usuario informa o ID "109" e o novo local "Biblioteca"
    When envia a solicitacao de atualizacao
    Then o sistema atualiza o local do item no arquivo
