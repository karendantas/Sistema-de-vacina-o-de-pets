from datetime import datetime
from abc import ABC, abstractmethod
from src.models.animal import Animal
from src.utilities.gerencia_csv import Gerencia_csv
'''
    Arquivo dedicado ao gerenciamento das super classes(Usuario, Pessoa)
 
'''
class AutenticavelMixIn(Gerencia_csv):
   
    def autentica(self):
        '''
        Pede o login e a senha de um usuário, as informações serão verificadas em um método
        da classe 'Gerencia_csv' que retorna um Boolen para confirmar a verificação
    
        '''
        login = input("Informe o seu login: ")
        senha = input("Informe sua senha: ")
        super().autentica_usuario('src\Database\Banco_Cliente.csv', login, senha)
        
      

#Interface Usuário
class Usuario(ABC, AutenticavelMixIn, Gerencia_csv):
    def __init__(self, login, email, senha ):
        self.__login = login
        self.__senha = senha
        self.email = email

    #Gets e Sets
    def getLogin(self):
        return self.__login
    def setLogin(self, novologin):
        self.__login = novologin
        return self.__login
    def getSenha(self):
        return self.__senha
    def setSenha(self, novasenha):
        self.__senha = novasenha
        return self.__senha 

    @abstractmethod
    def Cadastrar_pet(self):
        '''Usuário informa dados sobre o animal, instanciando um objeto do tipo animal
          e a função retorna a instancia'''
        nome_pet = input("Informe o nome do animal: ")
        data_pet = str(input("Informe a data de nascimento do animal:"))
        formato = "%d/%m/%Y"
        data_pet = datetime.strptime(data_pet, formato)
        data_pet = data_pet.date()
        raça_pet = input("Informe a reaça do animal: ")
        sexo_pet = input("Informe o sexo do animal: ")
        especie_pet = input("Informe a especie do animal:")

        animal = Animal(nome_pet, raça_pet, especie_pet, data_pet,sexo_pet )

        dados = [[nome_pet, raça_pet, data_pet, especie_pet, data_pet, sexo_pet]]
        Gerencia_csv().escrever_arquivo("src\Database\Banco_Animais.csv", dados)

        return animal
    
    @abstractmethod
    def Agendar_vacina(self, data, Animal, Cliente, Agenda, Vacina):
        #lembrando que antes precisa mostrar para o cliente as datas disponiveis
        
        '''Esse metodo irá receber os args e irá alocar em um dict. 
           Esse dict irá ser alocado na classe Agenda por meio do metódo set_agendamentos

            Args:
            data: uma string no formato datetime
            animal: (object) uma instancia da classe Animal
            cliente: (object) uma instancia da classe Cliente
            agenda: (object) uma instancia da classe Agenda
            vacina: (object) uma instancia da classe Vacina
        '''
        #conferindo se a data digitada está disponível
        if Gerencia_csv.verificar_datas(data):
            agendamento = {}
            agendamento = {"Cliente: ": Cliente,"Animal: ":Animal,"Data: ":data,"Vacina: ":Vacina}
            Agenda.set_agendamentos(agendamento)
        else:
            print("Desculpe, a data informada não é válida.")
    
    @abstractmethod
    def Aplicar_vacina(self,animal,vacina,aplicador,aplicacao_vacina):
        if aplicador is None:
            print("Não foi possível efetuar a vacinação")
        else:
            aplicacao_vacina.data_aplicacao = datetime.today()
            animal.setHistoricoVacinas("Vacina: {}\nAplicador: {}\nData aplicação Vacina: {}".format(vacina.nome,
            aplicador.nome_completo,aplicacao_vacina.data_aplicacao))
            #chamar funcao que remove uma vacina
            # Gerencia_csv.remove_vacinas(vacina.nome)

class Pessoa:
    def __init__(self, nome_completo, data, telefone, cpf):
        self.nome_completo = nome_completo
        self.data_nascimento = data
        self.telefone = telefone
        self.__cpf = cpf

    #Gets e Sets
    def getCpf(self):
        return self.__cpf
    def setCpf(self, novocpf):
        self.__cpf = novocpf
        return self.__cpf
