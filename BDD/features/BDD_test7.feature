Feature: Filtrar itens por data
  Como usuario do sistema
  Quero filtrar os itens por uma data especifica
  Para visualizar apenas os itens registrados nessa data

  Scenario: Filtrar itens pela data 06/06/2025
    Given o usuario informa a data "06/06/2025"
    When envia a solicitacao de filtro
    Then o sistema retorna todos os itens com a data "06/06/2025"
