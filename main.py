# from src.utilities.gerencia_csv import Gerencia_csv
# from src.models.cliente import Cliente
# from src.models.vacina import Vacina
# import re
from datetime import datetime
# cli = Cliente("a","a","a","a","a","a","a")
# # print(cli.animais)

# vacina1 = Vacina('Vacina1', '20mg', 'None', '21123')
# g = Gerencia_csv()
# # g.inicia_arquivo('src\Database\Banco_Vacinas.csv')

# vacina =[['nome3', '30mg', 'nenhuma', '21/21/21', '5']]
# # g.escrever_arquivo('src\Database\Banco_Vacinas.csv', vacina)
# # g.remove_vacinas('src\Database\Banco_Vacinas.csv', 'nome2')

# g.inicia_arquivo('src\Database\Banco_Cliente.csv')


# #O PROBLEMA ERAM OS ESPACINHOS
# cli.autentica()
# g.inicia_arquivo('src\Database\Banco_Datas.csv')
infinito = 1
while infinito != 0:
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
                    login = input("Informe o login: ")
                    senha = input("Informe a senha: ")
                    if (cli.autentica(login,senha) == True):
                        while infinito != 0:
                            print("1 - Cadastrar Pet")
                            print("2 - Agendar Vacina")
                            print("3 - Aplicar Vacina")
                            print("4 - Sair")
                            opcao3 = int(input("Digite sua opção: "))
                            match opcao3:
                                case 1:
                                    cli.Cadastrar_pet()
                                case 2:
                                    data = str(input("Informe uma data: "))
                                    animal = str(input("Informe o nome do aninal: "))
                                    vacina = str(input("Informe o nome da vacina: "))
                                    formato = "%d/%m/%Y"
                                    data = datetime.strptime(data, formato)
                                    data = data.date()
                                    for i in cli.animais:
                                       if (i.nome == animal):
                                           animal = i
                                    cli.Agendar_vacina(data,animal,cli,agenda,vacina)
                                case 3:
                                    cli.Aplicar_vacina()
                                case 4:
                                    infinito = 0
                    else:
                        print("Não foi possivel encontrar seu cadastro")
                    
        case 2:

        case 3:
            infinito = 0

