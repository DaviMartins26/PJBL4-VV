Feature: Cadastro de item perdido
  Como usuário do sistema
  Quero cadastrar um item perdido
  Para que ele seja registrado corretamente

  Scenario: Cadastro de um item perdido com dados válidos
    Given o sistema está pronto para cadastrar itens perdidos
    When cadastrar um item com id "111", nome "Gabriel Vettorazzi", descrição "Carteira preta", data "10/06/2025", local "Confeitaria Holandesa" e status "perdido"
    Then o sistema deve confirmar que o cadastro foi realizado com sucesso
