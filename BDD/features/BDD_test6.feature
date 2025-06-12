Feature: Listar itens achados
  Como usuário do sistema
  Quero visualizar todos os itens que foram encontrados
  Para que possam ser devolvidos aos seus donos

  Scenario: Exibir todos os itens com tipo achado
    Given que o arquivo de itens já existe e contém registros
    When o usuario solicita listar os itens do tipo achado
    Then o sistema exibe apenas os itens marcados como achado
