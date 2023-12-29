from datetime import datetime
from src.models.cliente import Cliente
from src.models.usuario import Usuario
from src.models.animal import Animal
from src.models.funcionarios import Funcionario, Aplicador
from src.utilities.gerencia_csv import Gerencia_csv
from src.models.estoque_vacina import Agenda
import csv


#Objetos definidos
agenda_sistema = Agenda()
aplicador_obj = Aplicador("Fernanda Biquinho", "12/02/1833", "21 32333212", "132.132.333-22", "Doutura")




opcao = 0
while opcao != 3:
    print("Olá, Bem vindo ao Sistema de Vacinação de Pets")
    print("1 - Cliente")
    print("2 - Funcionário")
    print("3 - Sair")
    opcao = int(input("Digite sua opção: "))

    match opcao:
        case 1:
            print("1 - Já é Cliente")
            print("2 - Ainda não é Cliente")
            opcao2 = int(input("Digite sua opção: "))
            match opcao2:
                case 1:
                    login = input("Informe seu login:")
                    senha = input("Informe senha:")
                    verificacao = Cliente.autentica_usuario(Cliente, 'src\Database\Banco_Cliente.csv', login, senha)
                    if (verificacao == True):
                        #Caso cliente seja autenticado, cria-se um objeto a partir dos dados armazenados
                        cliente_obj = ''
                        with open ("src\Database\Banco_Cliente.csv", mode ='r') as arq:
                                leitor_csv = csv.reader(arq, delimiter=',')
                                next(leitor_csv)
                                for atributo in leitor_csv:
                                    if atributo[4] == login:
                                        cliente_obj = Cliente(atributo[0], atributo[1], atributo[2], atributo[3], atributo[4], atributo[5], atributo[6])
                        opcao3 = 0
                        while opcao3 != 4:
                            print("1 - Cadastrar Pet")
                            print("2 - Agendar Vacina")
                            print("3 - Aplicar Vacina")
                            print("4 - Sair")
                            opcao3 = int(input("Digite sua opção: "))
                            match opcao3:
                                case 1:
                                    #os inputs estao dentro do metodo que o objeto chama, e ele retorna o animla
                                    cliente_obj.Cadastrar_pet()
                                case 2:
                                    data = str(input("Informe uma data: "))
                                    animal = str(input("Informe o nome do aninal: "))
                                    vacina = str(input("Informe o nome da vacina: "))
                                    for i in cliente_obj.animais:
                                       if (i.nome == animal):
                                           animal = i
                                    cliente_obj.Agendar_vacina(data,animal,cliente_obj,agenda_sistema,vacina)
                                case 3:
                                    cliente_obj.Aplicar_vacina()
                                case 4:
                                    break
                    else:
                        print("Não foi possivel encontrar seu cadastro")

                case 2:
                    nome = input("Informe seu nome:")
                    data = str(input("Informe uma data: "))
                    formato = "%d/%m/%Y"
                    data = datetime.strptime(data, formato)
                    data = data.date()
                    telefone = str(input("Informe seu telefone:"))
                    cpf = str(input("Informe seu cpf"))
                    login = str(input("Crie um login: "))
                    senha = str(input("Crie uma senha:"))
                    email =str(input("Informe seu email:"))

                    cliente_objeto = Cliente(nome, data, telefone, cpf, login, senha, email)
                    dados = [[nome, data, telefone, cpf, login, senha, email]]
                    Gerencia_csv.escrever_arquivo(Gerencia_csv,"src\Database\Banco_Cliente.csv", dados)

                    
        case 2:
            print("TELA DO FUNCIONÁRIO")
            #autenticando funcionario
            login = input("Informe o login: ")
            senha = input("Informe a senha: ")
            verificacao = Funcionario.autentica_funcionario(Funcionario,"src\Database\Banco_Funcionarios.csv",login,senha)
            if (verificacao == True):
                #Caso funcionario seja autenticado, cria-se um objeto a partir dos dados armazenados
                funcionario_obj = ''
                with open ("src\Database\Banco_Funcionarios.csv", mode ='r') as arq:
                        leitor_csv = csv.reader(arq, delimiter =',')
                        next(leitor_csv)
                        for atributo in leitor_csv:
                            if atributo[6] == login:
                                funcionario_obj = Funcionario(atributo[0], atributo[1], atributo[2], atributo[3], atributo[4], atributo[5], atributo[6], atributo[7], atributo[8])

            print("1- Cadastrar um novo cliente")
            print("2 - Cadastrar um animal")
            print("3 - Verificar datas de vacinações disponíveis")
            print("4 - Verificar vacinas disponíveis")
            print("5 - Agendar uma vacincação")
            print("6 - Aplicar uma vacina")
            print("7 - Sair")
            opcao4 = 0

            while opcao4 !=7:
                opcao4 = int(input("Digite sua opção: "))
                match (opcao4):
                    case 1:
                        #funcionario pega os dados do cliente e adiciona no banco de dados
                        nome_cli = input("Nome do cliente: ")
                        data = str(input("Data do cliente: "))
                        formato = "%d/%m/%Y"
                        data = datetime.strptime(data, formato)
                        data = data.date()
                        telefone = str(input("Telefone do cliente"))
                        cpf = str(input("CPF do cliente: "))
                        login = str(input("Login do cliente: "))
                        senha = str(input("Senha do cliente:"))
                        email =str(input("Email do cliente:"))

                        dados_cliente = [[nome_cli, data, telefone,cpf, login, senha, email]]
                        cliente_obj1 = Cliente(nome_cli, data, telefone,cpf, login, senha, email)
                        funcionario_obj.escrever_arquivo('src/Database/Banco_Cliente.csv', dados_cliente)
                    case 2:
                        nome_cli = input("Informe o nome do cliente: ")

                        cliente_obj1 = ''
                        with open ("src/Database/Banco_Cliente.csv", mode ='r') as arq:
                                leitor_csv = csv.reader(arq, delimiter =',')
                                next(leitor_csv)
                                for atributo in leitor_csv:
                                    if atributo[0] == nome_cli:
                                        cliente_obj1 = Cliente(atributo[0], atributo[1], atributo[2], atributo[3], atributo[4], atributo[5], atributo[6])

                        animal_obj = ''
                        animal_obj = Usuario.Cadastrar_pet(Usuario)
                    case 3:
                        Gerencia_csv.ler_arquivo('src\Database\Banco_Datas.csv')
                    case 4:
                        Gerencia_csv.ler_arquivo('src\Database\Banco_Vacinas.csv')
                    case 5:
                        data = str(input("Informe uma data: "))
                        animal = str(input("Informe o nome do aninal: "))
                        vacina = str(input("Informe o nome da vacina: "))
                        formato = "%d/%m/%Y"
                        data = datetime.strptime(data, formato)
                        data = data.date()
                        for i in cliente_obj1.animais:
                            if (i.nome == animal):
                                animal = i
                        funcionario_obj.Agendar_vacina(data, animal, cliente_obj1, agenda_sistema, vacina)
                    case 6:
                        funcionario_obj.Aplicar_vacina(vacina, animal, aplicador_obj)
                    case 7:
                        break
        case 3:
            break

