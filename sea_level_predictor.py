# Importação das bibliotecas

#  Função principal

#  Ler os dados

#  Gráfico de dispersão (dados originais)

#  Regressão linear com **todos os dados**

#  Regressão linear desde o ano 2000

#  Configuração do gráfico

#  Salvar e retornar

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Dados históricos")

    # Create first line of best fit
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = range(1880, 2051)
    pred_all = [res_all.intercept + res_all.slope * year for year in years_all]
    plt.plot(years_all, pred_all, "r", label="Previsão (todos os dados)")

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_2000 = range(2000, 2051)
    pred_2000 = [res_2000.intercept + res_2000.slope * year for year in years_2000]
    plt.plot(years_2000, pred_2000, "green", label="Previsão (desde 2000)")

    # Add labels and title
    plt.ylabel("Nível do mar (pés)")
    plt.title("Previsão do aumento do nível do mar")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    return plt.gca()
