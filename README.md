# megasena-benford-law

# Mega Sena Benford's Law Analysis

Este projeto contém uma função chamada `benford_law()` que analisa a distribuição dos primeiros dígitos de uma lista de números de acordo com a Lei de Benford. A função é aplicada a um conjunto de dados contendo todos os resultados da Mega Sena armazenados em um arquivo CSV.

## Requisitos

- Python 3.x
- Pandas

## Instalação

1. Clone este repositório ou faça o download dos arquivos.
2. Instale a biblioteca pandas, caso ainda não tenha feito isso, executando `!pip install pandas` no terminal ou na célula de um notebook Jupyter.

## Uso

1. Atualize o caminho do arquivo CSV no script `megasena-benford-law.py` para corresponder ao local do arquivo em seu computador.
2. Execute o script `megasena-benford-law.py` para analisar os números da Mega Sena de acordo com a Lei de Benford e exibir a distribuição dos primeiros dígitos.

## Código

```python
# Importando as bibliotecas necessárias
import pandas as pd
from collections import Counter
import numpy as np

# Função para aplicar a Lei de Benford aos números da Mega Sena
def benford_law(numbers_list):
    first_digits = [int(str(num)[0]) for num in numbers_list]
    counter = Counter(first_digits)
    total_digits = len(first_digits)
    
    digit_frequencies = {digit: count / total_digits for digit, count in counter.items()}
    
    return digit_frequencies

# Carregue o arquivo CSV (altere o caminho do arquivo conforme necessário)
file_path = "caminho do arquivo csv"
df = pd.read_csv(file_path, sep=";")

# Extraia os números da Mega Sena
megasena_numbers = df[['numero 1', 'numero 2', 'numero 3', 'numero 4', 'numero 5', 'numero 6']].values.flatten()

# Aplique a função benford_law() aos números extraídos
benford_result = benford_law(megasena_numbers)

# Mostre os resultados
for digit, frequency in sorted(benford_result.items()):
    print(f"{digit}: {frequency * 100:.1f}%")

