# Celso Rodrigues Rocha Júnior
# Projeto - Sea Level Predictor
# Turma 19, Ateliê 12, Grupo 4

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Lê os dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Cria o gráfico de dispersão (scatter plot) com os dados existentes
    plt.figure(figsize=(10, 7))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.5, label='Observed Data')

    # Cria a primeira linha de melhor ajuste usando todos os dados
    # Usa regressão linear para encontrar a inclinação e interceptação
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Cria anos para previsão até 2050
    years_extended = pd.Series(range(1880, 2051))
    line_fit = slope * years_extended + intercept
    
    # Plota a linha de melhor ajuste
    plt.plot(years_extended, line_fit, color='red', label='Trend Line (1880-2050)')

    # Cria a segunda linha de melhor ajuste usando dados a partir de 2000
    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        recent_df['Year'],
        recent_df['CSIRO Adjusted Sea Level']
    )
    
    # Cria anos para previsão de 2000 até 2050
    years_recent = pd.Series(range(2000, 2051))
    line_fit_recent = slope_recent * years_recent + intercept_recent
    
    # Plota a segunda linha de melhor ajuste
    plt.plot(years_recent, line_fit_recent, color='green', label='Trend Line (2000-2050)')

    # Adiciona rótulos e título ao gráfico
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Ajusta o layout para evitar cortes nos rótulos
    plt.tight_layout()
    
    # Salva o gráfico e retorna os dados para teste (NÃO MODIFICAR)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
    # roda main