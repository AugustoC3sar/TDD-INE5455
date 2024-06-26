from src.funcionario import Funcionario
from src.ocorrencia import Ocorrencia

class Projeto:
    def __init__(self, id: int, titulo: str, custo: float, prazo: str, gerente: Funcionario, equipe:list):
        self.__id = id
        self.__titulo = titulo
        self.__custo = custo
        self.__prazo = prazo
        self.__gerente = gerente
        self.__equipe = equipe
        if gerente not in equipe:
            self.__equipe.append(self.__gerente)
        self.__ocorrencias = []
        self.__ocorrenciaId = 1

    @property
    def id(self):
        return self.__id
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def prazo(self):
        return self.__prazo
    
    @property
    def gerente(self):
        return self.__gerente
    
    @property
    def equipe(self):
        return self.__equipe

    @property
    def ocorrencias(self):
        return self.__ocorrencias

    def adicionarAEquipe(self, funcionario: Funcionario):
        if funcionario not in self.__equipe:
            self.__equipe.append(funcionario)
    
    def criarOcorrencia(self, resumo: str, responsavel: Funcionario, tipo: str, prioridade: int):
        if responsavel not in self.__equipe:
            raise ValueError("Responsável da ocorrência não pertence ao projeto")
    
        ocorrencia = Ocorrencia(self.__ocorrenciaId, resumo, responsavel, tipo, prioridade)
        responsavel.adicionarOcorrencia(ocorrencia)
        self.__ocorrencias.append(ocorrencia)
        self.__ocorrenciaId += 1
        return ocorrencia

    def encontrarOcorrencia(self, id_ocorrecia):
        for ocorrencia in self.__ocorrencias:
            if (ocorrencia.id == id_ocorrecia):
                return ocorrencia
        return None

    def finalizarOcorrencia(self, id_ocorrencia):
        for ocorrencia in self.__ocorrencias:
            if (ocorrencia.id == id_ocorrencia):
                ocorrencia.finalizar()
                ocorrencia.responsavel.removerOcorrencia(ocorrencia.id)
                self.__ocorrencias.remove(ocorrencia)
                break
