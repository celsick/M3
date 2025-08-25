import numpy as np

def calculate(numbers):
    # Conferindo se recebemos exatamente 9 valores
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Transformamos a lista em uma matriz 3x3
    matriz = np.array(numbers).reshape(3, 3)

    # Criamos um dicionário vazio para guardar os resultados
    resultados = {}

    # Definimos as operações que queremos calcular
    operacoes = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum
    }

    # Para cada operação, calculamos por coluna, por linha e no geral
    for nome, funcao in operacoes.items():
        por_coluna = funcao(matriz, axis=0).tolist()
        por_linha = funcao(matriz, axis=1).tolist()
        total = float(funcao(matriz))

        resultados[nome] = [por_coluna, por_linha, total]

    return resultados


# Exemplo de uso
if __name__ == "__main__":
    print(calculate([0,1,2,3,4,5,6,7,8]))
