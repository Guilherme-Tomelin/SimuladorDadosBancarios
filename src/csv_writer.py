#Módulo contendo a classe responsável por escrever os dados simulados em arquivos CSV.

import csv

class EscritorCSV:
    def escrever_dados(self, dados, nome_arquivo='saida.csv'):
        with open(nome_arquivo, 'w', newline='') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=dados[0].keys())
            #escritor.writeheader()
            escritor.writerows(dados)
