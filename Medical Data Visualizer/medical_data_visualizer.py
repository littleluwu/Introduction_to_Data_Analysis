import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# 1
current_file = os.path.abspath(os.path.dirname(__file__))
df = pd.read_csv(os.path.join(current_file, 'medical_examination.csv'))

# 2
bmi = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (bmi > 25) * 1

# 3
df['cholesterol'] = (df['cholesterol'] > 1) * 1
df['gluc'] = (df['gluc'] > 1) * 1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,
                id_vars=['cardio'],
                value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio']).value_counts().rename('total')
    
    # 7
    df_cat = df_cat.astype('long').to_frame()

    # 8
    fig = sns.catplot(data=df_cat,
                  x='variable',
                  y='total',
                  hue='value',
                  col='cardio',
                  order=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'],
                  kind='bar').fig


    # 9
    fig.savefig('Medical Data Visualizer/catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    #diastolic pressure is higher than systolic
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])]

    #height is less than the 2.5th percentile
    df_heat = df_heat[(df_heat['height'] >= df_heat['height'].quantile(0.025))]
    #height is more than the 97.5th percentile
    df_heat = df_heat[(df_heat['height'] <= df_heat['height'].quantile(0.975))]

    #weight is less than the 2.5th percentile
    df_heat = df_heat[(df_heat['weight'] >= df_heat['weight'].quantile(0.025))]
    #weight is more than the 97.5th percentile
    df_heat = df_heat[(df_heat['weight'] <= df_heat['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(10, 10))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt="0.1f", center=0, vmax=.8, cbar_kws = {'shrink':0.5})

    # 16
    fig.savefig('Medical Data Visualizer/heatmap.png')
    return fig
