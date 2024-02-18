def graficos_por_categoria(cat):
    """
        Recebe uma categoria como paramêtro, retorna uma lista, a qual:\n
        ~> Índice 0: lista os gráficos\n
        ~> Índice 1: descrição da categoria.

        :param cat: String
    """
    if cat == 'Óbitos':
        return [ ['Total de óbitos', 'Novos óbitos'], 'Em memória das vítimas do Corona Vírus. :latin_cross:' ]
    elif cat == 'Casos':
        return [ ['Total de casos','Novos casos', 'Suspeitos', 'Recuperados'], 'Dados relacionados ao surgimento de casos :hospital:']
    else: # cat == Vacinação
        return [ ['Vacinados', 'Vacinados por 100 habitantes', 'Vacinados segunda dose', 'Vacinados dose única', 'Vacinados terceira dose'] , 'Dados de vacinação :medical_symbol:' ]
    
def bandeira(estado):
    """
        Recebe um estado como paramêtro e retorna a bandeira deste.
        :param estado: String
    """
    match estado:
        # Nacional
        case 'TOTAL':
            return 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/800px-Flag_of_Brazil.svg.png'
        # Sudeste
        case 'SP':
            return 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Bandeira_do_estado_de_S%C3%A3o_Paulo.svg/800px-Bandeira_do_estado_de_S%C3%A3o_Paulo.svg.png'
        case 'MG':
            pass
        case 'RJ':
            pass
        case 'ES':
            pass
        # Nordeste
        case 'BA':
            pass
        case 'SE':
            pass
        case 'MA':
            pass
        case 'AL':
            pass
        case 'PE':
            pass
        case 'RN':
            pass
        case 'PB':
            pass
        case 'CE':
            pass
        case 'PI':
            pass
        # Centro-oeste
        case 'MT':
            pass
        case 'TO':
            pass
        case 'GO':
            pass
        case 'MS':
            pass
        # Norte
        case 'AM':
            pass
        case 'AC':
            pass
        case 'RR':
            pass
        case 'RO':
            pass
        case 'AP':
            pass
        case 'PA':
            pass
        # Sul
        case 'SC':
            pass
        case 'RS':
            pass
        case 'PR':
            pass