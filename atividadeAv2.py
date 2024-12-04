import csv

def apresentaRelatorio():
    try:
        with open("boletimSC.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            
            # Inicializa contadores
            numero_linhas = 0
            colunas = None
            
            for linha in leitor:
                if numero_linhas == 0:
                    # Primeira linha contém os nomes das colunas
                    colunas = linha
                numero_linhas += 1
            
            if numero_linhas > 0:
                print(f"Número total de linhas (incluindo cabeçalho): {numero_linhas}")
                print(f"Número de colunas: {len(colunas)}")
                print(f"Nomes das colunas: {', '.join(colunas)}")
            else:
                print("O arquivo está vazio.")
    
    except FileNotFoundError:
        print("Erro: O arquivo 'boletimSC.csv' não foi encontrado. Verifique o nome ou a localização do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chamar a função
apresentaRelatorio()
