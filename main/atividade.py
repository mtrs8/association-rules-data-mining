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
				if valor == 1:
					valores[j] = int(valor)
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