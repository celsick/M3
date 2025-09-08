# Celso Rodrigues Rocha Júnior
# Projeto - Page View Time Series Visualizer
# Turma 19, Ateliê 12, Grupo 4

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Importação e preparação dos dados
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    parse_dates=["date"],  # converte a coluna 'date' para datetime
    index_col="date"       # define 'date' como índice
)

# Faz toda a limpeza dos dados:
# Remove os 2,5% dias com menor e maior visualização
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]

# Gráfico de Linha
def draw_line_plot():
    
    fig, ax = plt.subplots(figsize=(15, 5))
    
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    fig.savefig("line_plot.png")
    return fig

# Gráfico de Barras
def draw_bar_plot():
    
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Agrupa por ano e mês, calcula média e reorganiza para plot
    df_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Plot
    fig, ax = plt.subplots(figsize=(15, 10))
    df_grouped.plot(kind="bar", ax=ax)
    
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(
        title="Months",
        labels=[
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
    )

    fig.savefig("bar_plot.png")
    return fig

# Cria o Box plot
def draw_box_plot():
    
    df_box = df.copy().reset_index()
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")

    fig, axes = plt.subplots(1, 2, figsize=(20, 10))

    # Box plot anual
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Box plot mensal
    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
