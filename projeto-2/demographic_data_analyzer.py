import pandas as pd

def calculate_demographic_data(print_data=True):
    # 1️⃣ Carregamos os dados do arquivo CSV
    dataset = pd.read_csv("adult.data.csv")

    # 2️⃣ Contamos quantas pessoas de cada raça existem
    race_count = dataset["race"].value_counts()

    # 3️⃣ Calculamos a idade média dos homens
    homens = dataset[dataset["sex"] == "Male"]
    average_age_men = round(homens["age"].mean(), 1)

    # 4️⃣ Percentual de pessoas com Bacharelado
    bacharelado = dataset[dataset["education"] == "Bachelors"]
    percentage_bachelors = round((len(bacharelado) / len(dataset)) * 100, 1)

    # 5️⃣ Percentual de pessoas com ensino avançado que ganham >50K
    educacao_avancada = dataset["education"].isin(["Bachelors", "Masters", "Doctorate"])
    pessoas_avancadas = dataset[educacao_avancada]
    pessoas_avancadas_ricas = pessoas_avancadas[pessoas_avancadas["salary"] == ">50K"]
    higher_education_rich = round((len(pessoas_avancadas_ricas) / len(pessoas_avancadas)) * 100, 1)

    # Percentual de pessoas sem ensino avançado que ganham >50K
    pessoas_basicas = dataset[~educacao_avancada]
    pessoas_basicas_ricas = pessoas_basicas[pessoas_basicas["salary"] == ">50K"]
    lower_education_rich = round((len(pessoas_basicas_ricas) / len(pessoas_basicas)) * 100, 1)

    # 6️⃣ Descobrimos quantas horas por semana as pessoas menos trabalham
    min_work_hours = dataset["hours-per-week"].min()

    # 7️⃣ Percentual de ricos entre quem trabalha o mínimo de horas
    trabalhadores_min = dataset[dataset["hours-per-week"] == min_work_hours]
    ricos_min = trabalhadores_min[trabalhadores_min["salary"] == ">50K"]
    rich_percentage = round((len(ricos_min) / len(trabalhadores_min)) * 100, 1)

    # 8️⃣ País com maior percentual de pessoas ricas
    percentuais_paises = (dataset[dataset["salary"] == ">50K"]["native-country"].value_counts() /
                          dataset["native-country"].value_counts()) * 100
    highest_earning_country = percentuais_paises.idxmax()
    highest_earning_country_percentage = round(percentuais_paises.max(), 1)

    # 9️⃣ Ocupação mais comum entre pessoas ricas na Índia
    indianos_ricos = dataset[(dataset["native-country"] == "India") & (dataset["salary"] == ">50K")]
    top_IN_occupation = indianos_ricos["occupation"].mode()[0]

    # 🔟 Exibir resultados, se desejado
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # 1️⃣1️⃣ Retornar todos os resultados em um dicionário
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }
