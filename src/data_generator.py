"""
Arquivo CSV é composto por:
Banco origem
Agência origem
Conta origem
Banco destino
Agência destino
Conta destino
Valor da transação
Data e hora da transação

Exemplo:

BANCO DO BRASIL,0001,00001-1,BANCO BRADESCO,0001,00001-1,8000,2022-01-01T07:30:00
BANCO SANTANDER,0001,00001-1,BANCO BRADESCO,0001,00001-1,210,2022-01-01T08:12:00
BANCO SANTANDER,0001,00002-1,BANCO BRADESCO,0001,00001-1,79800.22,2022-01-01T08:44:00
BANCO BRADESCO,0001,00001-1,BANCO SANTANDER,0001,00002-1,11.50,2022-01-01T12:32:00
BANCO BANRISUL,0001,00001-1,BANCO BRADESCO,0001,00001-1,100,2022-01-01T16:30:00
BANCO ITAU,0001,00001-1,BANCO BRADESCO,0001,00001-1,19000.50,2022-01-01T16:55:00
BANCO ITAU,0001,00002-1,BANCO BRADESCO,0001,00001-1,1000,2022-01-01T19:30:00
NUBANK,0001,00001-1,BANCO BRADESCO,0001,00001-1,2000,2022-01-01T19:34:00
BANCO INTER,0001,00001-1,BANCO BRADESCO,0001,00001-1,300,2022-01-01T20:30:00
CAIXA ECONOMICA FEDERAL,0001,00001-1,BANCO BRADESCO,0001,00001-1,900,2022-01-01T22:30:00
"""

# from faker import Faker
import random

bancos = [
    "BANCO DO BRASIL",
    "BANCO SANTANDER",
    "BANCO BRADESCO",
    "BANCO BANRISUL",
    "BANCO ITAU",
    "NUBANK",
    "BANCO INTER",
    "CAIXA ECONOMICA FEDERAL"
]

agencia = "0001"

conta = [
    "00001-1",
    "00002-1"
]




class GeradorDados:
    # def __init__(self):
    #     self.falso = Faker()

    def gerar_dados(self, num_linhas, data):
        dados = []
        for _ in range(num_linhas):
            numero_aleatorio = random.randint(100, 9999999) / 100

            hora = random.randint(0, 23)
            minutos = random.randint(0, 59)
            segundos = random.randint(0, 59)

            if hora < 10:
                hora = f"0{hora}"
            if minutos < 10:
                minutos = f"0{minutos}"
            if segundos < 10:
                segundos = f"0{segundos}"

            horario = f"{hora}:{minutos}:{segundos}"

            dados_linha = {
                "Banco Origem": random.choice(bancos),
                "Agência Origem": agencia,
                "Conta Origem": random.choice(conta),
                "Banco Destino": random.choice(bancos),
                "Agência Destino": agencia,
                "Conta Destino": random.choice(conta),
                "Valor da Transação": numero_aleatorio,
                "Data e Hora da Transação": f"{data}T{horario}"
            }
            dados.append(dados_linha)
        return dados
