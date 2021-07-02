from openpyxl import load_workbook

def fetch_data(file):
	wb = load_workbook(file)
	ws = wb['Página1']
	di = {}
	for row in ws.rows:
		for cell in row:
			if cell.value != None:
				key = str(cell).split(".")[1].split(">")[0]
				di[key] = cell.value
	return di

def get_values_cells(column, data):
	values = {}
	for i in data:
		if data[i] == column:
			letter, digit = i
			for j in range(int(digit) + 1, 12):
				value = data[letter + str(j)]
				if value == 'sim':
					values[j] = value
	return values

def compareTo(data1, data2):
	value = 0
	for i in data1:
		for j in data2:
			if i == j:
				if data1[i] == data2[j]:
					value += 1
	return value

def getProducts(data):
    values=[]
    for i in data:
        if len(i) == 2:
            letter, digit = i
            if digit == '1':
                if data[i] != 'None' and data[i] != 'TID':
                   values.append(data[i])
                   
    return values

def calculate_support_confidence(data, products, itens):
	for i in range(0, itens):
		x = get_values_cells(products[i], data)
		for j in range(0,itens):
			if i != j:
				y = get_values_cells(products[j], data)
				support= float(compareTo(x, y) / 10)
				confidence= float(compareTo(x, y) / len(x))
				print(products[i], "e", products[j],":")
				print(" Support: ", round(support, 2) )
				print(" Confidence:", round(confidence, 2))
				print("\n")