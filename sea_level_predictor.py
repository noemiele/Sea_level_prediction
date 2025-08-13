import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    path = 'epa-sea-level.csv'
    df = pd.read_csv(path)

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y)
    plt.scatter(x, y, label='CSIRO Adjusted Sea Level',color="blue")


    # Create first line of best fit
    fit1 = linregress(x, y)

    years_extension = np.arange(df['Year'].min(), 2051)
    prediction= fit1.intercept + fit1.slope * years_extension

    plt.plot(years_extension, prediction, color='red', label=f'Best Fit Line: y={fit1.slope:.2f}x+{fit1.intercept:.2f}')
    #plt.plot(years_extended_full, sea_level_predicted_full, color='red', label=f'Predicted Sea Level (1880 onwards to 2050)\ny={fit1.slope:.2f}x + {fit1.intercept:.2f}')


    # Create second line of best fit
    df_copy=df.copy()  
    start_year = 2000
    df_copy = df_copy[(df_copy['Year'] >= start_year)] 

    fit2 = linregress(df_copy['Year'], df_copy['CSIRO Adjusted Sea Level'])

    years_extension_new = np.arange(df_copy['Year'].min(), 2051)
    sea_level_predicted_new = fit2.intercept + fit2.slope * years_extension_new
    plt.plot(years_extension_new, sea_level_predicted_new, color='green', label=f'Best Fit Line (from 2000)\ny={fit2.slope:.2f}x + {fit2.intercept:.2f}')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()