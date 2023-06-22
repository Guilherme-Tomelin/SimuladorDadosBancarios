#Módulo contendo a classe responsável por escrever os dados simulados em arquivos CSV.

import csv
import datetime

class EscritorCSV:
    def escrever_dados(self, dados, nome_arquivo='saida.csv'):
        with open(nome_arquivo, 'w', newline='') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=dados[0].keys())
            #escritor.writeheader()
            escritor.writerows(dados)

    def gera_nome_saida(self):
        data_atual = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        nome_arquivo = f"saida_{data_atual}.csv"
        return nome_arquivo
