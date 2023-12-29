from src.models.usuario import Pessoa
from src.models.cliente import Cliente
from src.models.usuario import Usuario
from src.utilities.gerencia_csv import Gerencia_csv
class Funcionario(Pessoa,Usuario,Gerencia_csv):
    def __init__(self, nome_completo, data_nascimento, telefone, cpf, salário, cargo,login,senha,email):
        super().__init__(nome_completo, data_nascimento, telefone, cpf)
        Usuario.__init__(self,login, senha, email)
        self.__salario = salário
        self.cargo = cargo

    #Gets e Sets
    def getSalario(self):
        return self.__salario
    def setSalario(self, novosalario):
        self.__salario = novosalario
        return self.__salario
    
    
    def Agendar_vacina(self, cliente, animal,data,agenda,vacina):
        cliente.Agendar_vacina(data, animal, cliente, agenda, vacina)    
    
    
    def Cadastrar_pet(self, cliente):
        if isinstance(cliente,Cliente):
            cliente.Cadastrar_pet()

    def Aplicar_vacina(self):
        pass


class Aplicador(Funcionario,Pessoa):
    def __init__(self, nome_completo, data_nascimento, telefone, cpf,formacao):
        Pessoa.__init__(self, nome_completo, data_nascimento, telefone, cpf)
        self.formacao = formacao
