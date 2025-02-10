import os
import shutil
import smtplib
from email.mime.text import MIMEText

# Função para mover arquivos
def mover_arquivos(origem, destino):
    try:
        shutil.move(origem, destino)
        print(f'Arquivo movido de {origem} para {destino}')
    except Exception as e:
        print(f'Erro ao mover o arquivo: {e}')

# Função para limpar uma pasta (remover arquivos)
def limpar_pasta(pasta):
    try:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
        print(f'Pasta {pasta} limpa!')
    except Exception as e:
        print(f'Erro ao limpar a pasta: {e}')

# Função para enviar e-mail (simples)
def enviar_email():
    try:
        msg = MIMEText('Este é um e-mail automatizado!')
        msg['Subject'] = 'Automação de Tarefas'
        msg['From'] = 'daiarthur053@gmail.com'
        msg['To'] = 'pedrofabro05@gmail.com'

        # Conectar ao servidor SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('daiarthur053@gmail.com', 'sescesenaC2@')

        # Enviar o e-mail
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {e}')

# Chamando as funções
mover_arquivos('origem.txt', 'destino.txt')
limpar_pasta('minha_pasta')
enviar_email()
