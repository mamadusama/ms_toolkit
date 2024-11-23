import matplotlib.pyplot as plt
import seaborn as sns

def pltch(df):
    """
    Plota um mapa de calor de correlações considerando apenas colunas numéricas.
    """
    # Selecionar apenas colunas numéricas
    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.empty:
        print("O DataFrame não contém colunas numéricas para calcular correlações.")
        return

    # Gerar o mapa de calor
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title('Mapa de Calor das Correlações')
    plt.show()


def plth(df, column):
    """
    Plota um histograma para uma coluna específica.
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histograma de {column}')
    plt.show()


