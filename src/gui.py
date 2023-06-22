#Módulo contendo a definição da interface gráfica utilizando PySide2.

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from PySide2.QtCore import Qt
from data_generator import GeradorDados
from csv_writer import EscritorCSV


class JanelaPrincipal(QMainWindow):
    """
    Classe JanelaPrincipal, que herda da classe QMainWindow. Essa classe representa a janela principal da aplicação e define as configurações iniciais da janela, como o título e as dimensões.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador de Dados Bancários")
        self.setGeometry(100, 100, 300, 200)

        #Widgets da interface gráfica.
        #caixas de texto(QLineEdit) para inserir quantidade de linhas e data.
        #botão(QPushButton) para geração de dados.
        #através do clicked.connect sempre que o botão for clicado, o método self.gerar_dados será chamado.
        self.caixa_texto_linhas = QLineEdit()
        self.caixa_texto_linhas.setPlaceholderText("Quantidade de linhas")
        
        self.caixa_texto_data = QLineEdit()
        self.caixa_texto_data.setPlaceholderText("Data (AAAA-MM-DD)")

        self.botao_gerar_dados = QPushButton("Gerar Dados")
        self.botao_gerar_dados.clicked.connect(self.gerar_dados)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Quantidade de Linhas:"))
        layout.addWidget(self.caixa_texto_linhas)
        layout.addWidget(QLabel("Data (AAAA-MM-DD):"))
        layout.addWidget(self.caixa_texto_data)
        layout.addWidget(self.botao_gerar_dados)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.statusBar().addWidget(QLabel("Desenvolvido por Guilherme Tomelin"))


    def gerar_dados(self):
        num_linhas = int(self.caixa_texto_linhas.text())
        data = self.caixa_texto_data.text()

        if num_linhas <= 0:
            QMessageBox.critical(self, "Erro", "A quantidade de linhas deve ser um número positivo.")
            return
        
        gerador_dados = GeradorDados()
        escritor_csv = EscritorCSV()
        dados = gerador_dados.gerar_dados(num_linhas, data)
        escritor_csv.escrever_dados(dados)

        QMessageBox.information(self, "Concluído", "Dados gerados e salvos em arquivo CSV.")
        self.caixa_texto_linhas.clear()
        self.caixa_texto_data.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec_())
