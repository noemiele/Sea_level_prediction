import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("C:\\Users\\tombe\\OneDrive\\Desktop\\Python\\epa-sea-level.csv")

    # Create scatter plot
    df.plot(kind = 'scatter', x = 'Year', y = 'CSIRO Adjusted Sea Level', title = 'Rise in Sea Level', figsize = (10,6))

    # Create first line of best fit
df_filtered = df.dropna(subset=['CSIRO Adjusted Sea Level'])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")

# Create x values from the start year to 2050
years_extended = np.arange(df_filtered['Year'].min(), 2051)

# Compute predicted sea level using the regression line
sea_level_predicted = slope * years_extended + intercept

# Plot scatter plot
df_filtered.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level', title='Rise in Sea Level', figsize=(10, 6))

# Plot line of best fit
plt.plot(years_extended, sea_level_predicted, color='red', label='Line of Best Fit (to 2050)')

# Labels and legend
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level (mm)')
plt.legend()
plt.tight_layout()
    

    # Create second line of best fit
# Filter out NaNs and select only from 2000 onward
df_recent = df.dropna(subset=['CSIRO Adjusted Sea Level'])
df_recent = df_recent[df_recent['Year'] >= 2000]

# Perform linear regression on recent data (2000 to latest)
slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
    df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

# Create x values from 2000 to 2050
years_extended_recent = np.arange(2000, 2051)
sea_level_predicted_recent = slope_recent * years_extended_recent + intercept_recent

# Plot the original scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'], label='Data (2000–Recent)', alpha=0.6)

# Plot the recent line of best fit
plt.plot(years_extended_recent, sea_level_predicted_recent, color='green', label='Best Fit Line (2000–2050)')



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
