import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Load data
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    """Menggambar diagram sebar dan dua garis regresi linear untuk memprediksi kenaikan muka air laut hingga tahun 2050."""
    
    # Membuat scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", alpha=0.5)

    # Garis regresi pertama: Menggunakan semua data
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = np.arange(1880, 2051)
    plt.plot(years_extended, slope * years_extended + intercept, 'r', label="Best fit line (1880-2050)")

    # Garis regresi kedua: Menggunakan data sejak tahun 2000
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = np.arange(2000, 2051)
    plt.plot(years_recent, slope_recent * years_recent + intercept_recent, 'g', label="Best fit line (2000-2050)")

    # Label dan judul
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Simpan dan kembalikan gambar
    plt.savefig("sea_level_plot.png")
    return plt.gca()
