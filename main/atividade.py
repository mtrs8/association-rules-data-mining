from openpyxl import load_workbook

def carregar_dados(file):
	wb = load_workbook(filename=file)
	ws = wb['tabela-de-transacao']
	di = {}
	for row in ws.rows:
		for cell in row:
			if cell.value != None:
				chave = str(cell).split(".")[1].split(">")[0]
				di[chave] = cell.value
	return di

def valores_celulas(coluna, dados):
	valores={}
	for key in dados:
		if dados[key] == coluna:
			letra, digito = key
			for i in range(int(digito)+1,12):
				valor = dados[letra + str(i)]
				if valor == 1:
					valores[i] = int(valor)
	return valores

def calculo_comparativo(dados1, dados2):
	valor = 0
	for i in dados1:
		for j in dados2:
			if i == j:
				if dados1[i] == dados2[j]:
					valor += 1
	return valor

def getProdutos(dados):
    valores=[]
    for key in dados:
        if len(key) ==2:
            letra, digito = key
            if digito == '1':
                if dados[key] != 'None' and dados[key] != 'TID':
                   valores.append(dados[key])
                   
    return valores