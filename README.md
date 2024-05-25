## Verificar coverage

`coverage run -m unittest discover -s tests`
`coverage html`

## Lista de Testes

### Empresa
- Teste 1: Criação de empresa: Empresa()
- Teste 2: Cadastrar funcionário: Empresa.cadastrarFuncionario()
- Teste 3: Não cadastrar funcionário com nome inválido: Empresa.cadastrarFuncionario()
- Teste 4: Não cadastrar funcionário com CPF inválido: Empresa.cadastrarFuncionario() e Empresa.\_\_validaCPF()
- Teste 5: Não cadastrar funcionário com cargo inválido: Empresa.cadastrarFuncionario()
- Teste 6: Não cadastrar funcionário com salário inválido: Empresa.cadastrarFuncionario()
- Teste 7: Cadastrar mais de um funcionário: Empresa.cadastrarFuncionario()
- Teste 8: Não cadastrar funcionário que já está cadastrado: Empresa.cadastrarFuncionario()
- Teste 9: Encontrar funcionário registrado na empresa: Empresa.encontrarFuncionario()
- Teste 10: Não encontrar funcionário não registrado na empresa: Empresa.encontrarFuncionario()
- Teste 11: Criar projeto sem equipe: Empresa.novoProjeto()
- Teste 12: Criar projeto com equipe de funcionários registrados na empresa: Empresa.novoProjeto()
- Teste 13: Não criar projeto com equipe que possui algum funcionário que não está registrado na empresa: Empresa.novoProjeto()
- Teste 14: Encontrar projeto registrado: Empresa.encontrarProjeto()
- Teste 15: Não encontrar projeto que não foi registrado: Empresa.encontrarProjeto()
- Teste 16: Insere funcionário em projeto: Empresa.adicionarAoProjeto()
- Teste 17: Não insere funcionário que não foi registrado em projeto: Empresa.adicionarAoProjeto()
- Teste 21: Não insere funcionário registrado em projeto inexistente: Empresa.adicionarAoProjeto()

### Funcionário
- Teste 18: Criação de funcionário: Funcionario()
- Teste 28: Adicionar ocorrência a lista de ocorrências do funcionario: Funcionario.adicionarOcorrencia()
- Teste 29: Remover ocorrência da lista de ocorrências do funcionario: Funcionario.removerOcorrencia()

### Projeto
- Teste 19: Criação de projeto: Projeto()
- Teste 20: Adicionar funcionario a equipe: Projeto.adicionarAEquipe()
- Teste 24: Incluir ocorrência em projeto: projeto.criarOcorrencia()

### Ocorrencia
- Teste 22: Criação de Ocorrencia: Ocorrencia()
- Teste 23: Finalizar ocorrencia: Ocorrencia.finalizarOcorrencia()
- Teste 25: Modificar Prioridade da ocorrencia: Ocorrencia.modificarPrioridade()
- Teste 26: Não modifica prioridade da ocorrência para valor inválido: Ocorrencia.modificarPrioridade()
- Teste 27: Alterar o responsável da ocorrência: Ocorrencia.alterarResponsavel()