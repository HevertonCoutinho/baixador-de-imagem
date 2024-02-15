import os
import requests
import csv
from urllib.parse import urlparse

def baixar_imagens_do_csv(arquivo_csv, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    with open(arquivo_csv, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for i, linha in enumerate(leitor_csv):
            if not linha:
                continue

            link = linha[0].strip()

            print(f'Tentando baixar imagem {i + 1} do link: {link}')

            try:
                resposta = requests.get(link)
                resposta.raise_for_status()

                # Extrai o nome do arquivo da URL
                nome_arquivo = os.path.join(pasta_destino, os.path.basename(urlparse(link).path))

                with open(nome_arquivo, 'wb') as arquivo_imagem:
                    arquivo_imagem.write(resposta.content)

                print(f'Imagem {i + 1} baixada com sucesso: {nome_arquivo}')
            except Exception as e:
                print(f'Erro ao baixar imagem {i + 1}: {str(e)}')

# Substitua com o caminho do seu arquivo CSV
arquivo_csv = 'lista.csv'

# Substitua com o caminho da pasta onde você deseja salvar as imagens
pasta_destino = 'resultados'

baixar_imagens_do_csv(arquivo_csv, pasta_destino)
