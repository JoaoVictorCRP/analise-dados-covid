def graficos_por_categoria(cat):
    """Recebe uma categoria como paramêtro. retorna uma lista, a qual:\n
        ~> Índice 0: lista os gráficos\n
        ~> Índice 1: descrição da categoria.
    """
    if cat == 'Óbitos':
        return [ ['Total de óbitos', 'Novos óbitos'], 'Em memória das vítimas do Corona Vírus. :latin_cross:' ]
    elif cat == 'Casos':
        return [ ['Total de casos','Novos casos', 'Suspeitos', 'Recuperados'], 'Dados relacionados ao surgimento de casos :hospital:']
    else: # cat == Vacinação
        return [ ['Vacinados', 'Vacinados por 100 habitantes', 'Vacinados segunda dose', 'Vacinados dose única', 'Vacinados terceira dose'] , 'Dados de vacinação :medical_symbol:' ]