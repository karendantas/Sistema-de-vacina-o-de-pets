from src.utilities.gerencia_csv import ler_arquivo, escrever_arquivo

'''
    Arquivo dedicado as classes que gerenciam datas, estoque de vacinas e agendamentos do sistema
    
'''

class Agenda:
    '''

    Classe reponsável por fornecer informações sobre as vacinas e datas de vacinações
    disponíveis e gerenciamento das datas.
    
    '''
    def __init__(self):
        self.vacinas = EstoqueVacinas()
        self.__agendamentos = []

    #Gets e Sets --
    def get_agendamentos(self):
        return self.__agendamentos
    
    def set_agendamentos(self,valor):
        self.__agendamentos.append(valor)


    def datas_disponiveis(self):
        '''
            Le um arquivo csv que contem string de datas

        '''
        ler_arquivo("Arquivos.csv\Banco_Vacinas.csv")
    
    def modificar_datas(self, data):
        '''
        Envia uma data (dentro de uma lista 'dados') 
        para um arquivo.csv direcionado as datas disponíveis

        Args: data(str) Data no formato dd/mm/aaaa 
        '''
        dados = [[data]]
        escrever_arquivo("Agendas\Banco_Vacinas", dados)
    
    def vacinas_disponiveis(self):
        '''
        Le um arquivo csv que contem strings das vacinas e suas respectivas quantidades

        '''
        print("Vacinas disponíveis no momento: ")
        ler_arquivo("Arquivos.csv\Banco_Vacinas.csv")
        


class EstoqueVacinas:
    def __init__(self):
        pass

    def mostrar_vacinas(self):
        '''
        Chama método 'ler_arquivo' da classe 'Gerencia_csv' e
        le um arquivo csv contendo as vacinas disponíveis do sistema

        '''
        ler_arquivo("ArquivosCSV\Banco_Vacinas.csv")

    def adiciona_vacina(self, nomevacina, quantidade):
        '''
        Adiciona uma nova vacina, e sua quantidade, ou apenas a quantidade de uma vacina existente.
        
        Args: 
        nomevacina(str): Referente ao nome da vacina
        quantidade(str): Referente a quantidade em estoque de uma vacina

        '''
        dados = [[nomevacina, quantidade]]
        escrever_arquivo("ArquivosCSV\Banco_Vacinas.csv", dados)
    

    #terminar esse (to quase, codigo ta la no gerencia_csv)
    def remove_vacina(self, vacina):
        '''funcionario precisa de permissao pra fazer isso'''