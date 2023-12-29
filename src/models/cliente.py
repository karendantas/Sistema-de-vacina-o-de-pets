from src.models.usuario import Pessoa, Usuario
from src.models.animal import Animal
from src.utilities.gerencia_csv import Gerencia_csv
import datetime

class Cliente(Pessoa, Usuario, Gerencia_csv):
    def __init__(self, nome_completo, data_nascimento, telefone, cpf, login, senha, email):
        Pessoa.__init__(self, nome_completo, data_nascimento, telefone, cpf)
        Usuario.__init__(self,login, senha, email)
        self.animais = []

    def Cadastrar_pet(self):
        '''
            O método 'Cadastrar_pet' está na classe 'Usuario', por isso
            está sendo chamada pela classe Pai. O retorno da classe gera um objeto de animal
            que sera armazenado na variavel 'animal'

            Depois que a variavel conter de certeza um objeto de animal, ele sera adiconado
            a lista de animais do cliente e os dados do objeto serao enviados para o arquivo
            'Banco_Animais'
        
        '''
        nome_pet = input("Informe o nome do animal: ")
        data_pet = str(input("Informe a data de nascimento do animal:"))
        formato = "%d/%m/%Y"
        data_pet = datetime.strptime(data_pet, formato)
        data_pet = data_pet.date()
        raça_pet = input("Informe a reaça do animal: ")
        sexo_pet = input("Informe o sexo do animal: ")
        especie_pet = input("Informe a especie do animal:")

        animal = Animal(nome_pet, raça_pet, especie_pet, data_pet,sexo_pet )
        self.animais.append(animal)

        dados = [[nome_pet, raça_pet, data_pet, especie_pet, data_pet, sexo_pet]]
        Gerencia_csv().escrever_arquivo("src\Database\Banco_Animais.csv", dados)

            
    def Agendar_vacina(self, data, animal, cliente, Agenda, vacina):
        '''
        Chama o método 'Agendar_vacina' da classe Pai que reliza a criação de um dicionário
        e aloca dentro do atributo lista 'agendamentos' da Agenda que está em 'estoque_funcionarios'.

        Args:
        data: 
        animal: (Object) Uma instancia de Animal
        cliente: (Object) Instancia de Cliente
        Agenda: (Object) Instancia de Agenda
        vacina: (Object) Uma instancia da Vacina a ser utilizada

        '''

        if Gerencia_csv.verificar_datas(Gerencia_csv,data):
            Usuario().Agendar_vacina(data, animal, cliente, Agenda, vacina)
        else:
            print("Data informada inválida")
    
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
        
        Usuario().Aplicar_vacina(animal,vacina,aplicador,aplicacao_vacina)