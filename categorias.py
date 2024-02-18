def graficos_por_categoria(cat):
    if cat == 'Óbitos':
        return ['Total de óbitos', 'Novos óbitos']
    elif cat == 'Casos':
        return ['Total de casos','Novos casos', 'Suspeitos', 'Recuperados']
    else: # cat == Vacinação
        return ['Vacinados', 'Vacinados por 100 habitantes', 'Vacinados segunda dose', 'Vacinados dose única', 'Vacinados terceira dose']