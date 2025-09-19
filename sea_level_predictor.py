import pandas as pd #Importa a biblioteca ppandas 
import matplotlib.pyplot as plt 
from scipy.stats import linregress 

def draw_plot():
    # Le os dados do arquivo CSV que contem informaçoes 
    df = pd.read_csv("epa-sea-level.csv")


    # Cria um gráfico de dispersao 
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])


    # Caucula os parametros da regressao linear
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    anos_todos = pd.Series(range(1880, 2051))
    previsao_todos = intercept + slope * anos_todos
    plt.plot(anos_todos, previsao_todos, color="red")


    # Filtra o DataFrame para pegar apenas os registros de 2000 ate o resto.
    df_2000 = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    anos_2000 = pd.Series(range(2000, 2051))
    previsao_2000 = intercept2 + slope2 * anos_2000
    plt.plot(anos_2000, previsao_2000, color="green")


    # Adiciona o título ao gráfico para melhor entendimento.
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")


    
    # Salva o gráfico gerado como um arquivo PNG.
    plt.savefig("sea_level_plot.png")
    return plt.gca()