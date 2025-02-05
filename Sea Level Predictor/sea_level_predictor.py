import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

def draw_plot():
    # Read data from file
    current_file = os.path.abspath(os.path.dirname(__file__))
    df = pd.read_csv(os.path.join(current_file, 'epa-sea-level.csv'))

    # Create scatter plot


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('Sea Level Predictor/sea_level_plot.png')
    return plt.gca()