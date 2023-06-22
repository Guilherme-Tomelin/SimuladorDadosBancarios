import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QDateEdit, QCalendarWidget
from PySide2.QtCore import QDate, Qt
from data_generator import GeradorDados
from csv_writer import EscritorCSV


class JanelaPrincipal(QMainWindow):
    """
            Classe JanelaPrincipal, que herda da classe QMainWindow. Essa classe representa a janela principal 
            da aplicação e define as configurações iniciais da janela, como o título e as dimensões.
    """
    def __init__(self):
        """
            Definição:
            - Inicializa a janela principal da aplicação.
            - Configura o título e as dimensões da janela.
            - Cria os widgets e define seu layout.
            - Conecta os botões aos métodos correspondentes.
            - Define a barra de status.
        """
        super().__init__()
        self.setWindowTitle("Simulador de Dados Bancários")
        self.setFixedSize(400, 350)  # Aumentamos o tamanho inicial da janela

        # Widgets da interface gráfica.
        self.caixa_texto_linhas = QLineEdit()
        self.caixa_texto_linhas.setPlaceholderText("Quantidade de linhas")

        self.caixa_data = QDateEdit()
        self.caixa_data.setDisplayFormat("yyyy-MM-dd")
        self.caixa_data.setCalendarPopup(True)
        self.caixa_data.setDate(QDate.currentDate())

        self.caixa_data.setButtonSymbols(QDateEdit.NoButtons)  # Remove os botões da caixa de data

        self.botao_gerar_dados = QPushButton("Gerar Dados")
        self.botao_gerar_dados.clicked.connect(self.click_gerar_dados)

        # self.botao_escolher_diretorio = QPushButton("Escolher Diretório")
        # self.botao_escolher_diretorio.clicked.connect(self.click_escolher_diretorio)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Quantidade de Linhas:"))
        layout.addWidget(self.caixa_texto_linhas)
        layout.addWidget(QLabel("Data:"))
        layout.addWidget(self.caixa_data)
        layout.addWidget(self.botao_gerar_dados)
        #layout.addWidget(self.botao_escolher_diretorio)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.statusBar().addWidget(QLabel("Desenvolvido por Guilherme Tomelin"))

    def click_gerar_dados(self):
        """
        Definição:
        - Função acionada quando o botão "Escolher Diretório" for clicado.
        - Permite ao usuário selecionar um diretório.
        - Exibe uma mensagem informando o diretório selecionado.
        """
        num_linhas = self.caixa_texto_linhas.text()
        data = self.caixa_data.date().toString("yyyy-MM-dd")

        if not num_linhas or not data:
            QMessageBox.critical(self, "Erro", "Por favor, preencha a quantidade de linhas e a data.")
            return

        try:
            num_linhas = int(num_linhas)
            if num_linhas <= 0:
                QMessageBox.critical(self, "Erro", "A quantidade de linhas deve ser um número positivo.")
                return
        except ValueError:
            QMessageBox.critical(self, "Erro", "A quantidade de linhas deve ser um número válido.")
            return

        gerador_dados = GeradorDados()  # Instância do gerador de dados
        dados = gerador_dados.gerar_dados(num_linhas, data)  # Gera os dados simulados

        escritor_csv = EscritorCSV()
        dialogo = QFileDialog(self)
        dialogo.setFileMode(QFileDialog.Directory)
        if dialogo.exec_():
            diretorio = dialogo.selectedFiles()[0]
            nome_arquivo = diretorio + "/" + escritor_csv.gera_nome_saida()
            escritor_csv.escrever_dados(dados, nome_arquivo)

            QMessageBox.information(self, "Concluído", "Dados gerados e salvos em arquivo CSV.")
            self.caixa_texto_linhas.clear()
            self.caixa_data.setDate(QDate.currentDate())
        else:
            QMessageBox.warning(self, "Diretório não selecionado", "Nenhum diretório foi selecionado. A operação foi cancelada.")

    def click_escolher_diretorio(self):
        """
        Definição:
        - Função acionada quando o botão "Escolher Diretório" for clicado.
        - Permite ao usuário selecionar um diretório.
        - Exibe uma mensagem informando o diretório selecionado.

        """
        dialogo = QFileDialog(self)
        dialogo.setFileMode(QFileDialog.Directory)
        if dialogo.exec_():
            diretorio = dialogo.selectedFiles()[0]
            QMessageBox.information(self, "Diretório escolhido", f"Diretório selecionado: {diretorio}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec_())
