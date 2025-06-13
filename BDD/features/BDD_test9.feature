Feature: Alteração do tipo de item para “devolvido”
  Como usuário do sistema de Achados e Perdidos
  Quero alterar o tipo de um item existente para “devolvido”
  Para que o status reflita que o item já foi devolvido

  Scenario: Alterar com sucesso o tipo do item 109 para “devolvido”
    Given o arquivo de itens está carregado com o item 109 do tipo "achado"
    When eu altero o tipo do item com id "109" para "devolvido"
    Then a operação deve ser bem-sucedida
    And o tipo do item com id "109" deve ser "devolvido"
