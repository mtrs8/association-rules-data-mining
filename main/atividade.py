from openpyxl import load_workbook

def fetch_data(file):
	wb = load_workbook(file)
	ws = wb['Página1']
	di = {}
	for row in ws.rows:
		for cell in row:
			if cell.value != None:
				chave = str(cell).split(".")[1].split(">")[0]
				di[chave] = cell.value
	return di

def get_values_cells(coluna, dados):
	valores = {}
	for i in dados:
		if dados[i] == coluna:
			letra, digito = i
			for j in range(int(digito) + 1, 12):
				valor = dados[letra + str(j)]
				if valor == 'sim':
					valores[j] = valor
	return valores

def compareTo(dados1, dados2):
	valor = 0
	for i in dados1:
		for j in dados2:
			if i == j:
				if dados1[i] == dados2[j]:
					valor += 1
	return valor

def getProducts(dados):
    valores=[]
    for i in dados:
        if len(i) == 2:
            letra, digito = i
            if digito == '1':
                if dados[i] != 'None' and dados[i] != 'TID':
                   valores.append(dados[i])
                   
    return valores

def calculate_support_trust(data, products, itens):
	for i in range(0, itens):
		x = get_values_cells(products[i], data)
		for j in range(0,itens):
			if i != j:
				y = get_values_cells(products[j], data)
				suporte= float(compareTo(x, y) / 10)
				confianca= float(compareTo(x, y) / len(x))
				print("\n", products[i], " e ", products[j])
				print("Suporte: ", round(suporte, 2) )
				print("Confiança:", round(confianca, 2))
				print("\n")