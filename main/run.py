# Atividade Data Mining - Implementação de algoritmos de regras de associação usando python
# Disciplina: Banco de dados 2
# Alunos: Matheus Alves e Matheus Macedo
    # Leia o Arquivo Readme para instruções.

from atividade import *
from pathlib import Path

path = Path("files/")

file = path / "tabela-de-transacao.xlsx"

data = fetch_data(file)
products = getProducts(data)
itens= len(products)

for i in range(0, itens):
    x = get_values_cells(products[i], data)
    for j in range(0,itens):
        if i != j:
            y = get_values_cells(products[j], data)
            suporte= float(compareTo(x, y) / 10)
            confianca= float(compareTo(x, y) / len(x))
            print("\n", products[i], " e ", products[j])
            print("Suporte: ", suporte)
            print("Confiança:", confianca)
            print("\n")
    
x_values = get_values_cells("leite", data)
y_values = get_values_cells("café", data)
suporte = float(compareTo(x_values, y_values)/10)
confianca= float(compareTo(x_values, y_values)/len(x_values))

print("\nLeite e café:")
print("Suporte:", suporte)
print("Confiança:", confianca)

x_values= get_values_cells("pão", data)
y_values= get_values_cells("manteiga", data)
suporte = float(compareTo(x_values, y_values)/10)
confianca = float(compareTo(x_values, y_values)/len(x_values))

print("\nPão e manteiga:")
print("Suporte:", suporte)
print("Confiança:", confianca)