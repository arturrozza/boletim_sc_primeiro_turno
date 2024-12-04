import csv
import os
import statistics

def apresentaRelatorio():
    try:
        with open("boletimSC.csv", "r") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")

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
        top_n = int(input("Digite o número de cidades que deseja listar (top N): "))

        with open(arquivOrigem, "r") as arquivo_origem:
            leitor = csv.reader(arquivo_origem, delimiter=";")
            cabecalho = next(leitor)  # Lê o cabeçalho
            
            # Índices das colunas relevantes
            indice_cidade = cabecalho.index("NM_MUNICIPIO")  # Ensure the correct column name
            indice_partido = cabecalho.index("SG_PARTIDO")  # Ensure the correct column name
            indice_votos = cabecalho.index("QT_VOTOS")
            
            # Filtra os dados
            dados_filtrados = [
                (linha[indice_cidade], int(linha[indice_votos]))
                for linha in leitor if linha[indice_partido].strip().lower() == filtroPartido.lower()
            ]
            
            # Ordena por número de votos em ordem decrescente
            dados_filtrados.sort(key=lambda x: x[1], reverse=True)
            dados_filtrados = dados_filtrados[:top_n]

            # Cria o arquivo de destino
            with open(arquivDestino, "w", newline="") as arquivo_destino:
                escritor = csv.writer(arquivo_destino)
                escritor.writerow(["Cidade", "Votos"])  # Cabeçalho do arquivo de destino
                escritor.writerows(dados_filtrados)  # Escreve os dados filtrados

            print(f"Arquivo '{arquivDestino}' criado com sucesso com os dados filtrados!")

    except FileNotFoundError:
        print("ERRO: O arquivo de origem não foi encontrado.")
    except ValueError:
        print("ERRO: Certifique-se de digitar um número válido para o top N.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def criaResumoArquivo():
    try:
        arquivOrigem = "boletimSC.csv"
        arquivResumo = input("Digite o nome do arquivo de resumo (exemplo.csv): ")

        with open(arquivOrigem, "r") as arquivo_origem:
            leitor = csv.reader(arquivo_origem, delimiter=";")
            cabecalho = next(leitor)  # Lê o cabeçalho

            # Índices das colunas relevantes
            indice_partido = cabecalho.index("SG_PARTIDO")
            indice_votos = cabecalho.index("QT_VOTOS")

            # Dicionário para armazenar os totais de votos por partido
            resumo_partidos = {}

            # Processa os dados e soma os votos por partido
            for linha in leitor:
                partido = linha[indice_partido].strip().lower()  # Usa .lower() para garantir que a comparação seja insensível a maiúsculas/minúsculas
                votos = int(linha[indice_votos]) if linha[indice_votos].isdigit() else 0  # Verifica se o valor de votos é um número válido

                if partido in resumo_partidos:
                    resumo_partidos[partido] += votos
                else:
                    resumo_partidos[partido] = votos

            # Cria o arquivo de resumo
            with open(arquivResumo, "w", newline="") as arquivo_destino:
                escritor = csv.writer(arquivo_destino)
                escritor.writerow(["Partido", "Total de Votos"])  # Cabeçalho do arquivo de resumo

                # Escreve os totais de votos por partido
                for partido, total_votos in resumo_partidos.items():
                    escritor.writerow([partido, total_votos])

            print(f"Arquivo de resumo '{arquivResumo}' criado com sucesso com os dados agregados!")

    except FileNotFoundError:
        print("ERRO: O arquivo de origem não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao criar o resumo: {e}")

def apresentaEstatisticas():
    try:
        votos = []  # Lista para armazenar os votos

        with open("boletimSC.csv", "r") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")
            cabecalho = next(leitor)  # Lê o cabeçalho

            # Índice da coluna de votos
            indice_votos = cabecalho.index("QT_VOTOS")

            # Coleta todos os votos na lista
            for linha in leitor:
                votos.append(int(linha[indice_votos]) if linha[indice_votos].isdigit() else 0)

        # Calculando estatísticas
        if votos:
            media = statistics.mean(votos)
            mediana = statistics.median(votos)
            desvio_padrao = statistics.stdev(votos) if len(votos) > 1 else 0  # Desvio padrão precisa de mais de um valor
            moda = statistics.mode(votos) if len(votos) > 1 else None  # Moda

            # Exibindo os resultados
            print(f"Média de votos: {media:.2f}")
            print(f"Mediana de votos: {mediana}")
            print(f"Desvio Padrão dos votos: {desvio_padrao:.2f}")
            print(f"Moda dos votos: {moda if moda is not None else 'Nenhuma moda encontrada'}")

        else:
            print("ERRO: Nenhum dado de votos encontrado no arquivo.")

    except FileNotFoundError:
        print("ERRO: O arquivo não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao calcular estatísticas: {e}")



def deletaArquivoCSV():
    try:
        arquivDestino = input("Digite o nome do arquivo que deseja excluir (exemplo.csv): ")

        # Verifica se o arquivo existe
        if os.path.exists(arquivDestino):
            os.remove(arquivDestino)  # Deleta o arquivo
            print(f"O arquivo '{arquivDestino}' foi excluído com sucesso!")
        else:
            print(f"ERRO: O arquivo '{arquivDestino}' não foi encontrado.")
    
    except Exception as e:
        print(f"Erro ao tentar excluir o arquivo: {e}")



