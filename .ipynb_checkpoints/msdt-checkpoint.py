import pandas as pd

def ld(file_path, sep=','):
    """
    Carrega um arquivo CSV em um DataFrame do Pandas.
    """
    try:
        return pd.read_csv(file_path, sep=sep)
    except Exception as e:
        print(f"Erro ao carregar o arquivo CSV: {e}")
        return None

def ldx(file_path):
    """
    Carrega um arquivo Excel em um DataFrame do Pandas.
    """
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Erro ao carregar o arquivo Excel: {e}")
        return None



# import pandas as pd

# def ld(filepath, ):
#     """
#     Carrega um arquivo CSV em um DataFrame do pandas.

#     Args:
#         filepath (str): Caminho para o arquivo CSV.
#         sep (str): Separador usado no arquivo. Padrão é ','.

#     Returns:
#         DataFrame: DataFrame carregado com os dados do CSV.
#     """
#     return pd.read_csv(filepath, sep=sep)
