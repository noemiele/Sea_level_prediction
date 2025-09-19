
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = np.arange(df['Year'].min(), 2051)
    y_all = res_all.intercept + res_all.slope * x_all
    plt.plot(x_all, y_all)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2000 = np.arange(2000, 2051)
    y_2000 = res_2000.intercept + res_2000.slope * x_2000
    plt.plot(x_2000, y_2000)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
