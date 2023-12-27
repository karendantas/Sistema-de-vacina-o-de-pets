from src.models.usuario import Pessoa
from src.models.cliente import Cliente

class Funcionário(Pessoa):
    def __init__(self, nome_completo, data_nascimento, telefone, cpf, salário, cargo):
        super().__init__(nome_completo, data_nascimento, telefone, cpf)
        self.__salario = salário
        self.cargo = cargo

    #Gets e Sets
    def getSalario(self):
        return self.__salario
    def setSalario(self, novosalario):
        self.__salario = novosalario
        return self.__salario
    
    
    # Lucas
    def Agendar_vacina(self, cliente, animal,data,agenda,vacina):
        cliente.Agendar_vacina(data, animal, cliente, agenda, vacina)    
    #
    
    
    def Cadastrar_pet(self, cliente, animal):
        if isinstance(cliente,Cliente):
            cliente.Cadastrar_pet(animal)

    def Aplicar_vacina(self):
        pass

# Lucas
class Aplicador(Funcionário,Pessoa):
    def __init__(self, nome_completo, data_nascimento, telefone, cpf,formacao):
        Pessoa.__init__(self, nome_completo, data_nascimento, telefone, cpf)
        self.formacao = formacao
