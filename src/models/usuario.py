from datetime import datetime
from abc import ABC, abstractmethod
from src.utilities.gerencia_csv import Gerencia_csv
'''
    Arquivo dedicado ao gerenciamento das super classes(Usuario, Pessoa)
 
'''


#Interface Usuário
class Usuario(ABC, Gerencia_csv):
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

    def Cadastrar_pet(self, Animal):
        '''Usuário informa dados sobre o animal, instanciando um objeto do tipo animal
          e a função retorna a instancia'''
        nome = input("Informe o nome do animal: ")
        raça = input("Informe a raça do animal: ")
        especie = input("Informe a espécie do animal: ")
        data_nascimento = input("Informe a data de nascimento: ")
        sexo = input("Informe o sexo do animal: ")

        animal = Animal(nome, raça, especie, data_nascimento, sexo)

        dados = [[nome, raça, data_nascimento]]
        super().escrever_arquivo("ArquivosCSV\Banco_Animais.csv", dados)

        return animal
    
    # Lucas
    @abstractmethod
    def Agendar_vacina(self,data,Animal,Cliente,Agenda,Vacina):
        '''Esse metodo irá receber os args e irá alocar em um dict. Esse dict irá ser alocado na classe Agenda por meio do metódo set_agendamentos'''

        '''
        Args:
            data: uma string no formato datetime
            animal: (object) uma instancia da classe Animal
            cliente: (object) uma instancia da classe Cliente
            agenda: (object) uma instancia da classe Agenda
            vacina: (object) uma instancia da classe Vacina
            '''
        agendamento = {}
        agendamento = {"Cliente: ": Cliente,"Animal: ":Animal,"Data: ":data,"Vacina: ":Vacina}
        Agenda.set_agendamentos(agendamento)
    
    @abstractmethod
    def Aplicar_vacina(self,animal,vacina,aplicador,aplicacao_vacina):
        if aplicador is None:
            print("Não foi possível efetuar a vacinação")
        else:
            aplicacao_vacina.data_aplicacao = datetime.today()
            animal.setHistoricoVacinas("Vacina: {}\nAplicador: {}\nData aplicação Vacina: {}".format(vacina.nome,
            aplicador.nome_completo,aplicacao_vacina.data_aplicacao))

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

class AutenticavelMixIn:
    '''Pede login e senha do usuário, retornando True caso o login e senha estejam de acordo
       com o cadastrado. Dessa forma, autenticando o usuário e permitindo certas ações dentro
       do sistema '''
    def autentica(self, usuario):
        login = input("Informe o seu login: ")
        senha = input("Informe sua senha: ")
        if login == usuario.getLogin() and senha == usuario.getSenha():
            return True