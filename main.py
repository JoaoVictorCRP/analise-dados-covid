import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')
# Mudando nomes das colunas
df = df.rename(columns={
    'epi_week': 'Semana epidemiológica',
    'date': 'Data',
    'country': 'País',
    'state': 'Estado',
    'city': 'Cidade',
    'newDeaths': 'Novos óbitos',
    'deaths': 'Total de óbitos',
    'newCases': 'Novos casos',
    'totalCases': 'Total de casos',
    'deathsMS': 'Óbitos MS',
    'totalCasesMS': 'Total de casos MS',
    'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes',
    'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes',
    'deaths_by_totalCases': 'Mortes por casos totais',
    'recovered': 'Recuperados',
    'suspects': 'Suspeitos',
    'tests': 'Testes realizados',
    'tests_per_100k_inhabitants': 'Testes por 100 mil habitantes',
    'vaccinated': 'Vacinados',
    'vaccinated_per_100_inhabitants': 'Vacinados por 100 habitantes',
    'vaccinated_second': 'Vacinados segunda dose',
    'vaccinated_second_per_100_inhabitants': 'Vacinados segunda dose por 100 habitantes',
    'vaccinated_single': 'Vacinados dose única',
    'vaccinated_single_per_100_inhabitants': 'Vacinados dose única por 100 habitantes',
    'vaccinated_third': 'Vacinados terceira dose',
    'vaccinated_third_per_100_inhabitants': 'Vacinados terceira dose por 100 habitantes'
})

estado_escolhido = 'SP'
estados = list(df['Estado'].unique())

coluna = 'Casos por 100 mil habitantes'
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']

# Filtrar por estado
df = df[df['Estado'] == estado_escolhido]

fig = px.line(df, x='Data', y=coluna, title=coluna+' - '+estado_escolhido)

fig.show()