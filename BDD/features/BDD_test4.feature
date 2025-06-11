Feature: Filtro de itens perdidos
  Como usuário do sistema
  Quero filtrar itens perdidos por critérios específicos
  Para encontrar rapidamente os itens desejados

  Scenario: Filtrar itens por local e status
    Given que existem os seguintes itens perdidos cadastrados
      | id  | nome    | descricao      | data       | local                | status    |
      | 111 | Gabriel | Carteira preta | 10/06/2025 | Confeitaria Holandesa | perdido   |
      | 112 | Ana     | Chave prata   | 09/06/2025 | Shopping Curitiba           | encontrado|
    When eu filtro os itens pelo local "Confeitaria Holandesa" e status "perdido"
    Then devo receber somente os itens que correspondem ao filtro
      | id  | nome    | descricao      | data       | local                | status    |
      | 111 | Gabriel | Carteira preta | 10/06/2025 | Confeitaria Holandesa | perdido   |
