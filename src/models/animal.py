from src.utilities.gerencia_csv import Gerencia_csv


class Animal(Gerencia_csv):
    def __init__(self, nome, raca, especie, data, sexo):
        self.nome = nome
        self.raça = Raca(raca)
        self.especie = Especie(especie)
        self.data_nascimento =  data
        self.sexo = sexo
        self.__historico_vacinas = []
        self.nome_cliente = ""

    #Gets e Sets
    def getHitoricoVacinas(self):
        return self.__historico_vacinas
    def setHistoricoVacinas(self, novavacina):
        self.__historico_vacinas.append(novavacina)
        return self.__historico_vacinas
    

class Raca:
    def __init__(self, nome_raça):
        self.nome_raça = nome_raça
class Especie:
    def __init__(self, nome_especie):
        self.nome_especie = nome_especie