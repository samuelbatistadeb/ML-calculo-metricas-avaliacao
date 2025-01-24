# Avaliação de Modelos de Classificação: Cálculo de Métricas

Este projeto tem como objetivo calcular e avaliar as principais métricas de desempenho de modelos de classificação, como **Acurácia**, **Sensibilidade (Recall)**, **Especificidade**, **Precisão** e **F-Score**. Utilizando uma matriz de confusão manualmente definida, o código permite entender a implementação de cada uma dessas métricas e sua importância na avaliação de modelos preditivos.

A matriz de confusão, composta pelos valores de **Verdadeiro Positivo (VP)**, **Verdadeiro Negativo (VN)**, **Falso Positivo (FP)** e **Falso Negativo (FN)**, é a base para o cálculo das métricas.

Além disso, o projeto utiliza a biblioteca `matplotlib` para exibir a matriz de confusão de forma visual, facilitando a compreensão dos resultados.

## Funcionalidades

- Cálculo das principais métricas de avaliação de classificação:
  - **Acurácia**
  - **Sensibilidade (Recall)**
  - **Especificidade**
  - **Precisão**
  - **F-Score**
- Visualização gráfica da matriz de confusão utilizando `matplotlib`.

## Tecnologias Utilizadas

- **Python 3**: Linguagem principal utilizada para o desenvolvimento.
- **Numpy**: Para manipulação de arrays e cálculos matemáticos.
- **Matplotlib**: Para visualização gráfica da matriz de confusão.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. Você pode verificar isso executando:

```bash
python --version
```
## Instalando as Dependências

Para instalar as bibliotecas `matplotlib` e `numpy` você pode executar o seguinte comando:

```bash
pip install numpy matplotlib
```
## Como Executar

Após instalar as dependências, siga os seguintes passos para rodar o projeto:

1. **Clone o repositório para sua máquina local**:

   Execute o comando abaixo no terminal para clonar o repositório:
   
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. **Navegue até o diretório do projeto**:

   Após clonar o repositório, acesse o diretório do projeto com o comando:
   
    ```bash
    cd nome-do-repositorio
    ```

3. **Execute o script Python**:

   Agora, execute o script principal do projeto para calcular as métricas e exibir a matriz de confusão com o seguinte comando:
   
    ```bash
    python calc-exib-metricas.py
    ```

Após rodar o código, o terminal exibirá as métricas calculadas (Acurácia, Sensibilidade, Especificidade, Precisão, F-Score). Além disso, a matriz de confusão será gerada em uma janela gráfica utilizando o `matplotlib`.

## Exemplo de Saída
Abaixo está um exemplo de saída que será exibido no terminal:

 ```bash
Acurácia: 0.85
Sensibilidade (Recall): 0.91
Especificidade: 0.80
Precisão: 0.83
F-Score: 0.87
```
E a matriz de confusão será apresentada de forma visual em uma janela do `matplotlib`.

## 

**Autor:** Samuel Batista 

**Data:** Janeiro de 2025
