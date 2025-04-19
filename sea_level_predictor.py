import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    # Read the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.6)

    # Create first line of best fit
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create second line of best fit
    # Predict values from 1880 to 2050
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_full = res_full.intercept + res_full.slope * years_extended
    plt.plot(years_extended, sea_levels_full, 'r', label='Best Fit Line (1880–2050)')

    # Filter data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]

    # Perform linear regression on recent data
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Predict values from 2000 to 2050
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = res_recent.intercept + res_recent.slope * years_recent
    plt.plot(years_recent, sea_levels_recent, 'g', label='Best Fit Line (2000–2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()