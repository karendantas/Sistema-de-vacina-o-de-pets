from src.models.usuario import Pessoa
from src.models.usuario import Usuario
from src.utilities.gerencia_csv import Gerencia_csv
import datetime
class Funcionario(Pessoa, Usuario, Gerencia_csv):
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
    
    def Cadastrar_Cliente(self):
        
        '''
            O método 'Cadastrar_Cliente' irá chamar vários inputs de dados diferente, na qual
            serão armazenados em uma lista dados clientes

            Depois essa variavel conter de certeza todos os dados de um objeto cliente, ela será enviada
            para o 'Banco_Cliente'
        
        '''


        nome_cli = input("Nome do cliente: ")
        data = str(input("Data de Nascimento do cliente: "))
        formato = "%d/%m/%Y"
        data = datetime.strptime(data, formato)
        data = data.date()
        telefone = str(input("Telefone do cliente: "))
        cpf = str(input("CPF do cliente: "))
        login = str(input("Login do cliente: "))
        senha = str(input("Senha do cliente: "))
        email =str(input("Email do cliente: "))

        dados_cliente = [[nome_cli, data, telefone,cpf, login, senha, email]]
        Gerencia_csv.escrever_arquivo(Gerencia_csv,'src/Database/Banco_Cliente.csv', dados_cliente)

    def Agendar_vacina(self, cliente, animal,data,agenda,vacina):
        pass 
    
    
    def Cadastrar_pet(self, cliente):
       pass

    def Aplicar_vacina(self):
        pass


class Aplicador(Funcionario,Pessoa):
    def __init__(self, nome_completo, data_nascimento, telefone, cpf,formacao):
        Pessoa.__init__(self, nome_completo, data_nascimento, telefone, cpf)
        self.formacao = formacao
