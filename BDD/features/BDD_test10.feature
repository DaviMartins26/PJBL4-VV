Feature: Alteração da senha de um usuário
  Como administrador do sistema
  Quero alterar a senha de um usuário específico
  Para que ele possa fazer login com a nova credencial

  Scenario: Alterar com sucesso a senha do usuário Daniel Lima
    Given o arquivo de usuários está carregado com o usuário "daniel.lima@email.com" com senha "senhaAntiga!"
    When eu altero a senha para "novaSenha123"
    Then a operação deve ser bem‐sucedida
    And o usuário com email "daniel.lima@email.com" deve ter a senha "novaSenha123"
