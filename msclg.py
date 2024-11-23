def dmv(df):
    """
    Remove valores ausentes de um DataFrame.
    """
    return df.dropna()

def dr(df):
    """
    Remove valores duplicados de um DataFrame.
    """
    return df.drop_duplicates()

def scn(df):
    """
    Padroniza os nomes das colunas (todas em minúsculas e sem espaços).
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df


def rm_cols(df, cols):
    """
    Remove colunas específicas de um DataFrame.
    
    Args:
        df (DataFrame): O DataFrame original.
        cols (list): Lista de colunas para remover.

    Returns:
        DataFrame: DataFrame atualizado sem as colunas especificadas.
    """
    return df.drop(columns=cols)