import pandas as pd
from collections import Counter
import numpy as np

def benford_law(numbers_list):
    first_digits = [int(str(num)[0]) for num in numbers_list]
    counter = Counter(first_digits)
    total_digits = len(first_digits)
    
    digit_frequencies = {digit: count / total_digits for digit, count in counter.items()}
    
    return digit_frequencies
# Carregue o arquivo CSV (altere o caminho do arquivo conforme necessário)
file_path = "C:/Users/thiago.gleal/Desktop/resultados_mega.csv"
df = pd.read_csv(file_path, sep=";")

# Extraia os números da Mega Sena
megasena_numbers = df[['numero 1', 'numero 2', 'numero 3', 'numero 4', 'numero 5', 'numero 6']].values.flatten()

# Aplique a função benford_law() aos números extraídos
benford_result = benford_law(megasena_numbers)

# Mostre os resultados
for digit, frequency in sorted(benford_result.items()):
    print(f"{digit}: {frequency * 100:.1f}%")
