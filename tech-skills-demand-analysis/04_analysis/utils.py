import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from adjustText import adjust_text

def bars_plot(df, relation, entity_name, title, xlabel = 'Developers', ylabel = '', top_n = 10, order = False, fmt = '{:,.0f}'):
    top = df[relation].sort_values(ascending = order).head(top_n).rename_axis(entity_name).reset_index(name=relation)
    fig, ax = plt.subplots(figsize = (7, 5))
    #norm = plt.Normalize(top[relation].min(), top[relation].max())
    #colors = plt.cm.viridis(norm(top[relation]))

    #bars = ax.barh(top[entity_name], top[relation], color = colors)
    #ax.bar_label(bars, fmt = fmt, padding = 3)
    bars = ax.barh(top[entity_name], top[relation], color='steelblue')
    ax.bar_label(bars, fmt = fmt, padding = 3)
    sns.despine(ax = ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.invert_yaxis()

    return ax

def bar_comparative_plot(df, category, title, xlabel = 'Developers', ylabel = '', top_n = 10, order = False):
    df_top = df.sort_values('HaveWorkedWith', ascending = order).head(top_n)
    df_long = df_top.reset_index().melt(
        id_vars = category,
        value_vars = ['Admired','HaveWorkedWith','WantToWorkWith'],
        var_name = 'Relation',
        value_name = 'Count'
    )
    df_long['Relation'] = df_long['Relation'].replace({
        'HaveWorkedWith': 'Used',
        'WantToWorkWith': 'Desired',
        'Admired': 'Admired'
    })
    order = ['Used','Desired','Admired']
    df_long['Relation'] = pd.Categorical(df_long['Relation'], categories=order, ordered=True)
    
    fig, ax = plt.subplots(figsize = (8, 5))
    sns.barplot(data=df_long, y=category, x='Count', hue='Relation', ax = ax)
    sns.despine(ax = ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(title='Relation')

    return ax

def assign_quadrant(df, x, y, x_median, y_median, name_col, top_right, top_left, bottom_left, bottom_right):
    df = df.copy()
    df.loc[(df[x] >= x_median) & (df[y] >= y_median), name_col] = top_right
    df.loc[(df[x] <  x_median) & (df[y] >= y_median), name_col] = top_left
    df.loc[(df[x] <  x_median) & (df[y] <  y_median), name_col] = bottom_left
    df.loc[(df[x] >= x_median) & (df[y] <  y_median), name_col] = bottom_right
    return df

def quadrant_chart(df, x, y, x_median, y_median, label_df, top_right, top_left, bottom_left, bottom_right, size = 'HaveWorkedWith'):
    df = df.copy()
    fig, ax = plt.subplots(figsize= (12,8))
    sns.scatterplot(
        data = df,
        x = x,
        y = y,
        size = size,
        sizes = (20, 300),
        alpha = 0.7,
        edgecolor='black',
        linewidth=0.3,
        ax = ax)

    texts = []
    for i in label_df.index:
        texts.append(ax.text(df.loc[i,x],df.loc[i,y],i,fontsize=9,))

    adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle='-', color='gray', lw=0.5))

    ax.axhline(y = y_median, color = 'black', linestyle ='--')
    ax.axvline(x = x_median, color = 'black', linestyle = '--')

    # limites del grafico
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # posiciones relativas
    x_left  = xlim[0] + (xlim[1]-xlim[0]) * 0.01
    x_right = xlim[0] + (xlim[1]-xlim[0])* 0.65

    y_top = ylim[0] + (ylim[1]-ylim[0]) * 0.92
    y_bottom = ylim[0] + (ylim[1]-ylim[0]) * 0.03

    # nombres de cuadrantes
    ax.text(x_right, y_top, top_right, fontsize=10, weight='bold')
    ax.text(x_left,  y_top, top_left, fontsize=10, weight='bold')
    ax.text(x_right, y_bottom, bottom_right, fontsize=10, weight='bold')
    ax.text(x_left,  y_bottom, bottom_left, fontsize=10, weight='bold')

    if ax.legend_:
        ax.legend_.set_title('Adoption size')

    return ax

