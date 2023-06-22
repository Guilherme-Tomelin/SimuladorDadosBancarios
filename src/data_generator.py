#Módulo contendo a classe responsável pela geração dos dados simulados utilizando a biblioteca Faker.

from faker import Faker

class GeradorDados:
    def __init__(self):
        self.falso = Faker()

    def gerar_dados(self, num_linhas, data):
        dados = []
        for _ in range(num_linhas):
            # Gerar dados simulados para cada linha
            # Exemplo: nome, sobrenome, número de conta, valor da transação, etc.
            dados_linha = {
                'nome': self.falso.name(),
                'sobrenome': self.falso.last_name(),
                'numero_conta': self.falso.random_int(min=1000, max=9999),
                'valor_transacao': self.falso.random_digit(),
                'data': data
            }
            dados.append(dados_linha)
        return dados
