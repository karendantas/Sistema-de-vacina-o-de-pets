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
        pass
    
    @abstractmethod
    def Agendar_vacina(self, data, Animal, Cliente, Agenda, Vacina):
        pass
    
    @abstractmethod
    def Aplicar_vacina(self,animal,vacina,aplicador,aplicacao_vacina):
        pass

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
