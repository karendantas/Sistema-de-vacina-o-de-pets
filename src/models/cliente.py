from src.models.usuario import Pessoa, Usuario
from src.models.animal import Animal
from src.utilities.gerencia_csv import Gerencia_csv

class Cliente(Pessoa, Usuario, Gerencia_csv):
    def __init__(self, nome_completo, data_nascimento, telefone, cpf, login, senha, email):
        Pessoa.__init__(self, nome_completo, data_nascimento, telefone, cpf)
        Usuario.__init__(self,login, senha, email)
        self.animais = []

    def Cadastrar_pet(self):
        '''Cria-se a instancia'''
        animal = super().Cadastrar_pet()
        if isinstance(animal, Animal):
            self.animais.append(animal)
        # Ajustei o metodo agendar vacina
    def Agendar_vacina(self, data, animal, cliente, Agenda, vacina):
        super().Agendar_vacina(data, animal, cliente, Agenda, vacina)
        return True
    
    def Aplicar_vacina(self,vacina, animal,aplicador,aplicacao_vacina):
        '''
        Simula a hora que o cliente leva o animal para receber a vacina, adicionando ao 
        histórico do animal a vacina recebida.

        Args:
        vacina: (Object) Uma instancia da Vacina a ser utilizada
        animal: (Object) Uma instancia de Animal
        aplicador: (Object) Uma instancia de Aplicador
        aplicacao_vacina: (Object) Uma instancia de Aplicacao_Vacina
        '''
        
        super().Aplicar_vacina(animal,vacina,aplicador,aplicacao_vacina)