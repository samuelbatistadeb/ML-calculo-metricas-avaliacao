import matplotlib.pyplot as plt
import numpy as np


# Definindo os valores arbitrários de VP, VN, FP e FN
VP = int(input("Qtd Verdadeiros Positivos:"))    # Verdadeiros Positivos
VN = int(input("Qtd Verdadeiros Negativos:"))    # Verdadeiros Positivos
FP = int(input("Qtd Falsos Positivos:"))    # Verdadeiros Positivos
FN = int(input("Qtd Falsos Negativos:"))    # Verdadeiros Positivos

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

# Criando a matriz de confusão
matriz_confusao = np.array([[VP, FP],  # [Verdadeiro Positivo, Falso Positivo]
                            [FN, VN]]) # [Falso Negativo, Verdadeiro Negativo]

# Função para exibir a matriz de confusão com matplotlib
def exibir_matriz_confusao(matriz):
    fig, ax = plt.subplots(figsize=(6, 5))  # Ajuste do tamanho da figura
    cax = ax.matshow(matriz, cmap="Blues")  # Usando o colormap "Blues" para visualização
    
    # Adicionando a barra de cores
    fig.colorbar(cax)
    
    # Definindo os rótulos
    ax.set_xticklabels(['', 'Predito: Negativo', 'Predito: Positivo'])
    ax.set_yticklabels(['', 'Real: Negativo', 'Real: Positivo'])
    
    # Adicionando os valores dentro das células
    for i in range(2):
        for j in range(2):
            ax.text(j, i, f'{matriz[i, j]}', ha='center', va='center', color='black', fontsize=14)

    # Ajustando os eixos
    ax.set_xlabel('Classes Preditas')
    ax.set_ylabel('Classes Reais')
    plt.title('Matriz de Confusão', fontsize=16)
    
    plt.show()

# Exibindo a matriz de confusão
exibir_matriz_confusao(matriz_confusao)