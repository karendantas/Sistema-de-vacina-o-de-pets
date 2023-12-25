import csv

''' Arquivo dedicado a funcoes de gerenciamento dos arquivos csv que simulam um banco de dados'''

class Gerencia_csv:
    def __init__(self):
        self.cabecalho_animais = ['Nome', 'Sexo','Data Nascimento','Histórico de Vacinas']
        self.cabecalho_clientes = ['Nome Completo','Data de Nascimento','Telefone','CPF','Login','Senha','Email']
        self.cabecalho_vacinas = ['Nome','Dosagem','Observações','Data de Vencimento','Quantidade']
        #fazer cabeçalhos csv

        pass
    def escrever_arquivo(caminho, dados):
        ''' 
        coleta dados e escreve em um arquivo csv
        
        Args:
        caminho(str): Referente ao camainho para o arquivo csv
        dados(list): Lista que contem outras listas de dados
            
        '''
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

    def remove_vacinas(caminho, dado):
        '''
            Procura no arquivo se a vacina que esta sendo requisitada existe, e armazena o inteiro
            da sua quantidade em uma variavel 'quantidade', para que seja retirada -1 do seu valor
            e jogar a modificação no arquivo ao final.

            Args: 
            caminho(str): caminho do arquivo csv
            dado(str): referente ao nome da vacina a ser modificada

        '''
        quantidade = 0
        with open(caminho, mode='r') as arquivopy:
            leitor_csv = csv.reader(arquivopy, delimiter=',')
            for linha in leitor_csv:
                if linha[0] == dado:
                    quantidade = int(linha[1])
                    print(quantidade)

    def limpar_csv(caminho):
        with open(caminho, mode='w') as arquivopy:
            escritor_csv = csv.writer(arquivopy, delimiter=',')
            escritor_csv.writerows=""
    def apagar_conteudo_arquivo_csv(caminho):
        cabeçalho=[]
        with open(caminho, mode='r') as arq:
            leitor = csv.reader(arq, delimiter=',')
            cabeçalho = next(leitor)

        # Abre o arquivo no modo de escrita, o que apaga o conteúdo existente
        with open(caminho, 'w', newline='', encoding='utf-8') as arq:
            escritor = csv.writer(arq, delimiter=',')
            escritor.writerow(cabeçalho)

# Gerencia_csv.ler_arquivo("Sistema-de-vacinacao-de-pets\Database\Banco_Cliente.csv")

