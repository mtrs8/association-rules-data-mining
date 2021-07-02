# Atividade Data Mining - Implementação de algoritmos de regras de associação usando python
# Disciplina: Banco de dados 2
# Alunos: Matheus Alves e Matheus Macedo
    # Leia o Arquivo Readme para instruções.

from atividade import calculate_support_trust, fetch_data, getProducts
from pathlib import Path

path = Path("files/")

file = path / "tabela-de-transacao.xlsx"

data = fetch_data(file)
products = getProducts(data)
itens= len(products)

calculate_support_trust(data, products, itens)