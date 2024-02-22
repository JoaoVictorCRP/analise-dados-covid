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
# Selecionar estado
estado_escolhido = st.selectbox('Estado', estados)
main_df = df[df['Estado'] == estado_escolhido]
# Barra lateral (Seleção de categoria)
with st.sidebar:
    categoria = st.selectbox('Categoria',opcoes)
#Compontentes
head1, head2 = st.columns(2)
with head1:
    st.title(categoria+' - '+estado_escolhido)
with head2:
    st.image(ex.bandeira(estado_escolhido),width=100)

descricao = ex.graficos_por_categoria(categoria)[1]
st.subheader(descricao)
op_week = st.toggle('Dados semanais', False)

if op_week:
    week = st.slider('Semana epidemiológica',9,311)
    main_df = df[df['Semana epidemiológica'] == week]
    st.subheader(':red[OBS: os dados da COVID-19 entre as semanas 153 e 200 não foram divulgados pelo ministério da saúde.]')

#Gráficos
graficos_pizza = ex.graficos_por_categoria(categoria)[0]
figs = []
for graf in graficos_pizza:
    fig = px.line(main_df, x='Data', y=graf)
    figs.append(fig)
#Colocando gráficos no streamlit
for fig in figs:
    st.plotly_chart(fig, use_container_width=True)

#Grafico de comparação entre dois estados
st.subheader('COMPARAR ESTADOS')
estado1 = st.selectbox('Estado Nº1', estados)
estado2 = st.selectbox('Estado nº2', estados)
df_estado1 = df[df['Estado'] == estado1]
df_estado2 = df[df['Estado'] == estado2]
df_comparacao = pd.concat([df_estado1, df_estado2])
fig_comparacao = px.line(df_comparacao, x='Data',y='Total de óbitos', color='Estado')
st.plotly_chart(fig_comparacao, use_container_width=True)
#Rodapé
st.caption('Dados retirados a partir do site: https://github.com/wcota/covid19br')