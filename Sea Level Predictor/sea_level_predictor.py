import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

def draw_plot():
    # Read data from file
    current_file = os.path.abspath(os.path.dirname(__file__))
    df = pd.read_csv(os.path.join(current_file, 'epa-sea-level.csv'))

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5)

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xseq = pd.Series([i for i in range(1880,2051)])
    plt.plot(xseq, res.intercept + res.slope * xseq, 'r')

    # Create second line of best fit
    res = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    xseq = pd.Series([i for i in range(2000,2051)])
    plt.plot(xseq, res.intercept + res.slope * xseq, 'blue')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('Sea Level Predictor/sea_level_plot.png')
    return plt.gca()