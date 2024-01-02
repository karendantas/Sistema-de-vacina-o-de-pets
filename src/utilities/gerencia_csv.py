import csv
import os
import re

''' Arquivo dedicado a funcoes de gerenciamento dos arquivos csv que simulam um banco de dados'''

class Gerencia_csv:
    def __init__(self):
        self.cabecalho_animais = ['Nome', 'Sexo','Data Nascimento','Histórico de Vacinas']
        self.cabecalho_clientes = ['Nome Completo','Data de Nascimento','Telefone','CPF','Login','Senha','Email']
        self.cabecalho_vacinas = ['Nome','Dosagem','Observacoes','Data de Vencimento','Quantidade']
        self.cabecalho_funcionarios = ['Nome Completo', 'Data de Nascimento', 'Telefone', 'CPF','Salario', 'Cargo','Login','Senha','Email']
        self.cabecalho_datas = ['Data']

        #fazer cabeçalhos csv

        pass

    #criei um arquivo de inicialização
    def inicia_arquivo(self, caminho):
        '''
        Verifica se o arquivo não existe, caso não exista, será iniciado novamente com 
        o respectivo cabeçalho
        
        '''
        if not os.path.exists(caminho):
            
            with open(caminho, mode = 'w', newline='') as arquivopy:
                escritor_csv = csv.writer(arquivopy, delimiter=',')
                cabecalho = self.retorna_cabecalho(caminho)
                escritor_csv.writerow(cabecalho)
        else:
            print("Arquivo existe!")

    #criei um procurador de cabeçalhos
    def retorna_cabecalho(self, caminho):

        '''
        O regex serve para verificar qual caminho do arquivo, e de acordo com o nome 'chave'
        do final do arquvivo, um cabeçalho especifico dessa chave sera usava para inicializar o 
        arquivo.

        Args:
        caminho(str): caminho do arquivo 
        
        '''
        re_clientes = r'.*\\.*\\.*_Cliente.csv'
        re_animais = r'.*\\.*\\.*_Animais.csv'
        re_datas = r'.*\\.*\\.*_Datas.csv'
        re_vacinas = r'.*\\.*\\.*_Vacinas.csv'
        re_funcionarios = r'.*\\.*\\.*_Funcionarios.csv'

        if re.search(re_clientes, caminho):
            return self.cabecalho_clientes
        
        if re.search(re_animais, caminho):
            return self.cabecalho_animais
        
        if re.search(re_datas, caminho):
            return self.cabecalho_datas
        
        if re.search(re_vacinas, caminho):
            return self.cabecalho_vacinas
        
        if re.search(re_funcionarios, caminho):
            return self.cabecalho_funcionarios
        
    def escrever_arquivo(self, caminho, dados):
        ''' 
        coleta dados e escreve em um arquivo csv
        
        Args:
        caminho(str): Referente ao camainho para o arquivo csv
        dados(list): Lista que contem outras listas de dados
            
        '''
        #self.inicia_arquivo(caminho) #verifica se arquivo existe
        with open(caminho, mode = 'a', newline='') as arquivopy:
            escritor_csv = csv.writer(arquivopy, delimiter=',')
            escritor_csv.writerows(dados)
            print("Dados armazenados")
        
        return True

    def ler_arquivo(caminho):
        '''
            Lê o conteúdo dentro do caminho de um arquivo csv

        '''
        with open (caminho, mode ='r') as arquivopy:
            leitor_csv = csv.DictReader(arquivopy, delimiter = ',')
            for linha in leitor_csv:
                print(linha)
                
        return True

    def remove_vacinas(self, caminho, nome_vacina):
        '''
            Procura no arquivo se a vacina que esta sendo requisitada existe, e armazena o inteiro
            da sua quantidade em uma variavel 'quantidade', para que seja retirada -1 do seu valor
            e jogar a modificação no arquivo ao final.

            Args: 
            caminho(str): caminho do arquivo csv
            nome_vacina(str): referente ao nome da vacina a ser modificada

        '''
        quantidade = 0
        linhas_atualiadas =[[]]
        with open(caminho, mode='r') as arquivopy:
            leitor_csv = csv.reader(arquivopy, delimiter=',')
            next(leitor_csv)
            for linha in leitor_csv:
                if linha == nome_vacina:
                    quantidade = int(linha[4]) -1
                    linha[4] = str(quantidade)
                    print(linha[4])
                linhas_atualiadas.append(linha)

        with open (caminho, mode = 'w', newline='') as arquivopy:
                 cabecalho = self.retorna_cabecalho(caminho)
                 escritor_csv  = csv.writer(arquivopy, delimiter=',')
                 escritor_csv.writerow(cabecalho)
                 escritor_csv.writerows(linhas_atualiadas)
            

    #criei uma autenticacao diretamente pelo csv
    def autentica_usuario(self, caminho, login, senha):
        '''
        Método que atua junto com método da classe Cliente, fazendo leitura e conferindo
        informação das linhas

        Args:
        login(str): Login de um usuario
        senha(str): Senha de um usuario

        Returns:
        Boolean: retorna True se a autenticação é um sucesso
        
        '''
        with open (caminho, mode='r') as arquivopy:
            Autenticacao = False
            leitor_csv = csv.reader(arquivopy, delimiter=',')
            next(leitor_csv)
            for linha in leitor_csv:
                if str(linha[4]) == login and str(linha[5]) == senha:
                    print("Autenticado!")
                    return True
                else:
                    Autenticacao = False
            if Autenticacao == False:
                print("Login ou senha incorretos")
                    

    def autentica_funcionario(self, caminho, login, senha):
        '''
        Método que atua junto com método da classe Cliente, fazendo leitura e conferindo
        informação das linhas do banco dos funcionarios, uma vez que ele tem mais informações.

        Args:
        login(str): Login de um usuario
        senha(str): Senha de um usuario

        Returns:
        Boolean: retorna True se a autenticação é um sucesso
        
        '''
        with open (caminho, mode='r') as arquivopy:
            Autenticacao = False
            leitor_csv = csv.reader(arquivopy, delimiter=',')
            next(leitor_csv)
            for linha in leitor_csv:
                if str(linha[6]) == login and str(linha[7]) == senha:
                    print("Autenticado!")
                    return True
                else:
                    Autenticacao = False
            if Autenticacao == False:
                print("Login ou senha incorretos")

    def verificar_datas(self, data):
        '''
        Verifica dentro do arquivo 'Banco_Datas' se existe uma data compatível com a que foi
        requisitada.

        Args:
        data():
        '''
        with open('src\Databse\Banco_Datas.csv', mode='r') as arquivopy:
            leitor_csv = csv.reader(arquivopy, delimiter=',')
            next(leitor_csv)
            for linha in leitor_csv:
                if linha[0] == data:
                    return True
    


