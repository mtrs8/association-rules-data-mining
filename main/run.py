from atividade import *

file = 'C:/Users/matheus.DESKTOP-MTRS8/pweb-env/bd_env/association-rules-data-mining/files/tabela-de-transacao.xlsx'

dados = carregar_dados(file)
produtos = getProdutos(dados)
itens= len(produtos)

for i in range(0,itens):
    x = valores_celulas(produtos[i], dados)
    for j in range(0,itens):
        if i != j:
            y = valores_celulas(produtos[j], dados)
            suporte= float(calculo_comparativo(x,y)/10)
            confianca= float(calculo_comparativo(x,y)/len(x))
            print("\n ", produtos[i], " e ", produtos[j])
            print("Suporte: ", suporte)
            print(" >Confiança:", confianca)
            print("\n")
    
x_valores= valores_celulas("leite", dados)
y_valores= valores_celulas("café", dados)
suporte = float(calculo_comparativo(x_valores,y_valores)/10)
confianca= float(calculo_comparativo(x_valores,y_valores)/len(x_valores))
print("\nLeite e café:")
print(" >Suporte:", suporte)
print(" >Confiança:", confianca)
x_valores= valores_celulas("pão", dados)
y_valores= valores_celulas("manteiga", dados)
suporte = float(calculo_comparativo(x_valores,y_valores)/10)
confianca= float(calculo_comparativo(x_valores,y_valores)/len(x_valores))
print("\nPão e manteiga:")
print(" >Suporte:", suporte)
print(" >Confiança:", confianca)