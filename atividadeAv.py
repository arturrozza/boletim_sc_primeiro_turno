import csv

def apresentaRelatorio():
    try:
        with open("boletimSC.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)

            numeroLinhas = 0
            colunas = None

            for linha in leitor:
                if numeroLinhas == 0:
                    colunas = linha
                numeroLinhas += 1

            if numeroLinhas > 0:
                print(f"Número de linhas (inclui cabeçalho): {numeroLinhas};")
                print(f"Número de colunas: {len(colunas)};")
                print(f"Nome das colunas: {', '.join(colunas)}.")
            else:
                print("Arquivo vazio.")

    except FileNotFoundError:
        print("ERRO: O arquivo não encontrado, verifique se o nome está correto.")
    
    except Exception as e:
        print(f"Erro inesperado: {e}")


def criaArquivParcial():
    try:
        arquivOrigem = "boletimSC.csv"
        arquivDestino = input("Digite o nome do arquivo destino (exemplo.csv): ")
        filtroPartido = input("Digite o partido para filtrar: ").strip()






# Função para criar um arquivo parcial com base na filtragem
# def criar_arquivo_parcial():
#     try:
#         nome_arquivo_origem = "boletimSC.csv"
#         nome_arquivo_destino = input("Digite o nome do arquivo de destino (inclua .csv): ")
#         partido_filtro = input("Digite o nome do partido para filtrar: ").strip()
#         top_n = int(input("Digite o número de cidades que deseja listar (top N): "))

#         with open(nome_arquivo_origem, "r") as arquivo_origem:
#             leitor = csv.reader(arquivo_origem)
#             cabecalho = next(leitor)  # Lê o cabeçalho
            
#             # Índices das colunas relevantes
#             indice_cidade = cabecalho.index("Cidade")
#             indice_partido = cabecalho.index("Partido")
#             indice_votos = cabecalho.index("Votos")
            
#             # Filtra os dados
#             dados_filtrados = [
#                 (linha[indice_cidade], int(linha[indice_votos]))
#                 for linha in leitor if linha[indice_partido].strip().lower() == partido_filtro.lower()
#             ]
            
#             # Ordena por número de votos em ordem decrescente
#             dados_filtrados.sort(key=lambda x: x[1], reverse=True)
#             dados_filtrados = dados_filtrados[:top_n]

#             # Cria o arquivo de destino
#             with open(nome_arquivo_destino, "w", newline="") as arquivo_destino:
#                 escritor = csv.writer(arquivo_destino)
#                 escritor.writerow(["Cidade", "Votos"])  # Cabeçalho do arquivo de destino
#                 escritor.writerows(dados_filtrados)  # Escreve os dados filtrados

#             print(f"Arquivo '{nome_arquivo_destino}' criado com sucesso com os dados filtrados!")

#     except FileNotFoundError:
#         print("ERRO: O arquivo de origem não foi encontrado.")
#     except ValueError:
#         print("ERRO: Certifique-se de digitar um número válido para o top N.")
#     except Exception as e:
#         print(f"Erro inesperado: {e}")









