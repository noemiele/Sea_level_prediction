import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # 1. Importar datos
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Crear scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data")

    # 3. Línea de mejor encaje para todo el conjunto de datos
    slope_all, intercept_all, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    years_extended = range(1880, 2051)
    sea_level_pred_all = [slope_all * year + intercept_all for year in years_extended]
    ax.plot(years_extended, sea_level_pred_all, "r", label="Fit: 1880-2050")

    # 4. Línea de mejor encaje desde el año 2000
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    years_recent = range(2000, 2051)
    sea_level_pred_recent = [slope_recent * year + intercept_recent for year in years_recent]
    ax.plot(years_recent, sea_level_pred_recent, "green", label="Fit: 2000-2050")

    # 5. Etiquetas y título
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Guardar y devolver figura
    fig.savefig("sea_level_plot.png")
    return fig
