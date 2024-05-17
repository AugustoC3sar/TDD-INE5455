## Verificar coverage

`coverage run -m unittest tests.{arquivoDeTeste}`
`coverage html`

## Lista de Histórias

## Lista de Testes

- Teste 1: Criação de empresa: Empresa()
- Teste 2: Cadastrar funcionário: Empresa.cadastrarFuncionario()
- Teste 3: Cadastrar funcionário com nome inválido: Empresa.cadastrarFuncionario()
- Teste 4: Cadastrar funcionário com CPF inválido: Empresa.cadastrarFuncionario() e Empresa.\_\_validaCPF()
- Teste 5: Cadastrar funcionário com cargo inválido: Empresa.cadastrarFuncionario()
- Teste 6: Cadastrar funcionário com salário inválido: Empresa.cadastrarFuncionario()
- Teste 7: Cadastrar mais de um funcionário: Empresa.cadastrarFuncionario()
- Teste 8: Cadastrar funcionário que já está cadastrado: Empresa.cadastrarFuncionario()
