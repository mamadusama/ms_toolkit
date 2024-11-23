def lpf(data, func):
    """
    Aplica uma função a todos os elementos de uma lista.
    """
    return [func(item) for item in data]

def fil(data, condition):
    """
    Filtra itens de uma lista com base em uma condição.
    """
    return [item for item in data if condition(item)]
