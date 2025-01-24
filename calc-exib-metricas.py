import matplotlib.pyplot as plt
import numpy as np


# Definindo os valores arbitrários de VP, VN, FP e FN
VP = 50  # Verdadeiros Positivos
VN = 40  # Verdadeiros Negativos
FP = 10  # Falsos Positivos
FN = 5   # Falsos Negativos

# Funções para calcular as métricas
def calcular_acuracia(VP, VN, FP, FN):
    return (VP + VN) / (VP + VN + FP + FN)

def calcular_sensibilidade(VP, FN):
    return VP / (VP + FN)

def calcular_especificidade(VN, FP):
    return VN / (VN + FP)

def calcular_precisao(VP, FP):
    return VP / (VP + FP)

def calcular_f_score(precisao, sensibilidade):
    return 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

# Calculando as métricas
acuracia = calcular_acuracia(VP, VN, FP, FN)
sensibilidade = calcular_sensibilidade(VP, FN)
especificidade = calcular_especificidade(VN, FP)
precisao = calcular_precisao(VP, FP)
f_score = calcular_f_score(precisao, sensibilidade)

# Exibindo os resultados
print(f"Acurácia: {acuracia:.2f}")
print(f"Sensibilidade (Recall): {sensibilidade:.2f}")
print(f"Especificidade: {especificidade:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"F-Score: {f_score:.2f}")
