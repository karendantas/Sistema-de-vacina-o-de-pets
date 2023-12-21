from src.utilities.gerencia_csv import Gerencia_csv
'''
    Arquivo dedicado a gerência da classe vacina e a classe AplicacaoVacina
'''
class Vacina(Gerencia_csv):

    def __init__(self,nome,dosagem,observacoes,data_vencimento):
        self.nome = nome
        self.__dosagem = dosagem
        self.observacoes = observacoes
        self.data_vencimento = data_vencimento

    # Gets e Sets
    def set_dosagem(self,valor):
        self.__dosagem = valor

    def get_dosagem(self):
        return self.__dosagem
    
class AplicacaoVacina:
    def __init__(self,data_aplicacao,ausente):
        self.data_aplicacao = data_aplicacao
        self.ausente = ausente
#