import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def predict_sea_level():
    # Charger les données
    df = pd.read_csv('epa-sea-level.csv')

    # Créer un graphique de dispersion
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Données réelles")

    # Ajouter une première ligne de régression (1880-2050)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)
    sea_level_extended = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_level_extended, 'blue', label="Tendance 1880-2050")

    # Ajouter une deuxième ligne de régression (2000-2050)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = range(2000, 2051)
    sea_level_recent_extended = [slope_recent * year + intercept_recent for year in years_recent_extended]
    plt.plot(years_recent_extended, sea_level_recent_extended, 'red', label="Tendance 2000-2050")

    # Ajouter des étiquettes et un titre
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Ajouter une grille et une légende
    plt.grid(True)
    plt.legend()

    # Sauvegarder l'image
    plt.savefig('sea_level_plot.png')

    # Afficher le graphique
    plt.show()
