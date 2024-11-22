import csv
import operator
from pathlib import Path


operaciones = {
    'SUM': operator.add,
    'SUB': operator.sub, 
    'MUL': operator.mul,
    'DIV': operator.truediv,
    'POW': operator.pow
}

def procesar_operaciones(archivo):
    resultados = []
    
    with open(archivo, 'r') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            operacion = fila['operation']
            op1 = float(fila['operand_1'])
            op2 = float(fila['operand_2'])
            
            if operacion == 'POW':
                if op2 > 10:
                    resultado = "fueraderango"
                else:
                    try:
                        resultado = operaciones[operacion](op1, op2)
                    except OverflowError:
                        resultado = "fueraderango"
            else:
                resultado = operaciones[operacion](op1, op2)
            
            resultados.append({
                'operation': operacion,
                'operand_1': op1,
                'operand_2': op2,
                'result': resultado
            })

    with open(archivo, 'w', newline='') as f:
        campos = ['operation', 'operand_1', 'operand_2', 'result']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)

archivo = Path('data/data.csv')

procesar_operaciones(archivo)
