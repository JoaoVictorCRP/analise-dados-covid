import pandas as pd
import plotly.express as px
import streamlit as st
import utils.externas as ex
# Lendo os dados
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
    'deaths_by_totalCases': 'Óbitos por casos totais',
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
# Lista de Estados
estados = list(df['Estado'].unique())
# Opcoes de categoria
opcoes = ['Óbitos', 'Casos', 'Vacinação']
# Selecionar categorias
categoria = st.selectbox('Categoria',opcoes)
graficos = ex.graficos_por_categoria(categoria)[0]
descricao = ex.graficos_por_categoria(categoria)[1]
# Barra lateral (Seleção de estado)
with st.sidebar:
    estado_escolhido = st.selectbox(
        "Estado",
        estados
    )
df = df[df['Estado'] == estado_escolhido]
#Compontentes
head1, head2 = st.columns(2)
with head1:
    st.title(categoria+' - '+estado_escolhido)
with head2:
    st.image(ex.bandeira(estado_escolhido),width=110)

st.subheader(descricao)
op_week = st.toggle('Dados semanais', False)

if op_week:
    week = st.slider('Semana epidemiológica',9,311)
    df = df[df['Semana epidemiológica'] == week]
    st.subheader(':red[OBS: os dados da COVID-19 entre as semanas 153 e 200 não foram divulgados pelo ministério da saúde.]')

#Gráficos
figs = []
for item in graficos:
    fig = px.line(df, x='Data', y=item)
    figs.append(fig)
#Colocando gráficos no streamlit
for node in figs:
    st.plotly_chart(node, use_container_width=True)
#Rodapé
st.caption('Dados retirados a partir do site: https://github.com/wcota/covid19br')