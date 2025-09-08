# Celso Rodrigues Rocha Júnior
# Projeto 3 - Medical Data Visualizer
# Turma 19, Ateliê 12, Grupo 4

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Carrega os dados
df = pd.read_csv("medical_examination.csv")

# Cria a coluna "overweight"
# IMC = peso (kg) / altura (m)^2
# Se IMC > 25 → overweight = 1 (sobrepeso), caso contrário 0
df["overweight"] = (df["weight"] / (df["height"] / 100) ** 2 > 25).astype(int)

# Normaliza colesterol e glicose
# 1 → 0 (normal / bom)
# >1 → 1 (acima do normal / ruim)
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)

# Gráfico Categórico
def draw_cat_plot():
    # Transforma dados para formato "longo"
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"],
    )

    # Agrupa dados por cardio, variável e valor
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # Cria gráfico categórico
    plot = sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        data=df_cat,
        kind="bar",
    )

    # Recupera figura
    fig = plot.fig

    # Salva o resultado!!
    fig.savefig("catplot.png")
    return fig

# Função: Heatmap de Correlação
def draw_heat_map():

    # Limpeza dos dados
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calcula matriz de correlação
    corr = df_heat.corr()

    # Cria máscara para triângulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Configura figura
    fig, ax = plt.subplots(figsize=(12, 12))

    # Cria heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )

    # Salva o resultado
    fig.savefig("heatmap.png")
    return fig