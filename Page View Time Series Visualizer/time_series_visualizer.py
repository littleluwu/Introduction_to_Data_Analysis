import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
current_file = os.path.abspath(os.path.dirname(__file__))
df = pd.read_csv(os.path.join(current_file, 'fcc-forum-pageviews.csv'))

# Clean data
df = df[df['value'] <= df['value'].quantile(0.975)]
df = df[df['value'] >= df['value'].quantile(0.025)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(21, 9))

    plt.plot(df['date'], df['value'])
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")


    # Save image and return fig (don't change this part)
    fig.savefig('Page View Time Series Visualizer/line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['date']  = pd.to_datetime(df['date'])
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month_name()

    df_bar.drop(columns=['date'],inplace=True)
    df_bar = df_bar.groupby(['year','month']).sum()

    fig = sns.catplot(data=df_bar,
                    x='year',
                    y='value',
                    hue='month',
                    hue_order=['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'],
                    order=['2016','2017','2018','2019'],
                    kind='bar',
                    palette='turbo',
                    height=6,
                    aspect=14/9)

    fig._legend.remove()
    plt.ticklabel_format(style='plain', axis='y')
    fig.set_xlabels('Years')
    fig.set_ylabels('Average Page Views')

    plt.legend(loc='upper left', title='Month')
    plt.tight_layout()

    fig = fig.fig

    # Save image and return fig (don't change this part)
    fig.savefig('Page View Time Series Visualizer/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['date']  = pd.to_datetime(df_box['date'])
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month_name()
    df_box['month'] = df_box['month'].str[:3]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(18, 5))

    sns.boxplot(
        data=df_box,
        x='year',
        y='value',
        hue='year',
        legend=False,
        palette='rainbow',
        ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    sns.boxplot(data=df_box,
                x='month',
                y='value',
                hue='month',
                legend=False,
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                palette='rainbow', ax=ax[1])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('Page View Time Series Visualizer/box_plot.png')
    return fig
