def graficos_por_categoria(cat):
    if cat == 'Óbitos':
        return ['Total de óbitos', 'Novos óbitos']
    elif cat == 'Casos':
        return ['Novos casos', 'Total de casos', 'Suspeitos', 'Recuperados']
    else: # cat == Vacina
        return ['Vacinados', 'Vacinados por 100 mil habitantes', 'Vacinados segunda dose', 'Vacinados dose única', 'Vacinados terceira dose']