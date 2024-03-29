def graficos_por_categoria(cat: str) -> list:
    """
        Recebe uma categoria como parâmetro, retorna uma lista, a qual:\n
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
    
def bandeira(estado: str) -> str:
    """
        Recebe um estado como parâmetro e retorna a bandeira deste.
        :param estado: String
    """
    # Nacional
    if estado == 'TOTAL':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/800px-Flag_of_Brazil.svg.png'
    elif estado == 'SP':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Bandeira_do_estado_de_S%C3%A3o_Paulo.svg/800px-Bandeira_do_estado_de_S%C3%A3o_Paulo.svg.png'
    elif estado == 'MG':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Bandeira_de_Minas_Gerais.svg/140px-Bandeira_de_Minas_Gerais.svg.png'
    elif estado == 'RJ':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Bandeira_do_estado_do_Rio_de_Janeiro.svg/140px-Bandeira_do_estado_do_Rio_de_Janeiro.svg.png'
    elif estado == 'ES':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Bandeira_do_Esp%C3%ADrito_Santo.svg/140px-Bandeira_do_Esp%C3%ADrito_Santo.svg.png'
    # Nordeste
    elif estado == 'BA':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Bandeira_da_Bahia.svg/140px-Bandeira_da_Bahia.svg.png'
    elif estado == 'SE':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Bandeira_de_Sergipe.svg/140px-Bandeira_de_Sergipe.svg.png'
    elif estado == 'MA':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Bandeira_do_Maranh%C3%A3o.svg/140px-Bandeira_do_Maranh%C3%A3o.svg.png'
    elif estado == 'AL':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Bandeira_de_Alagoas.svg/140px-Bandeira_de_Alagoas.svg.png'
    elif estado == 'PE':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Bandeira_de_Pernambuco.svg/140px-Bandeira_de_Pernambuco.svg.png'
    elif estado == 'RN':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Bandeira_do_Rio_Grande_do_Norte.svg/140px-Bandeira_do_Rio_Grande_do_Norte.svg.png'
    elif estado == 'PB':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Bandeira_da_Para%C3%ADba.svg/140px-Bandeira_da_Para%C3%ADba.svg.png'
    elif estado == 'CE':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Bandeira_do_Cear%C3%A1.svg/140px-Bandeira_do_Cear%C3%A1.svg.png'
    elif estado == 'PI':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Bandeira_do_Piau%C3%AD.svg/140px-Bandeira_do_Piau%C3%AD.svg.png'
    # Centro-oeste
    elif estado == 'MT':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Bandeira_de_Mato_Grosso.svg/140px-Bandeira_de_Mato_Grosso.svg.png'
    elif estado == 'TO':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Bandeira_do_Tocantins.svg/140px-Bandeira_do_Tocantins.svg.png'
    elif estado == 'GO':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_Goi%C3%A1s.svg/140px-Flag_of_Goi%C3%A1s.svg.png'
    elif estado == 'DF':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Bandeira_do_Distrito_Federal_%28Brasil%29.svg/140px-Bandeira_do_Distrito_Federal_%28Brasil%29.svg.png'
    elif estado == 'MS':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Bandeira_de_Mato_Grosso_do_Sul.svg/140px-Bandeira_de_Mato_Grosso_do_Sul.svg.png'
    # Norte
    elif estado == 'AM':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bandeira_do_Amazonas.svg/140px-Bandeira_do_Amazonas.svg.png'
    elif estado == 'AC':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Bandeira_do_Acre.svg/140px-Bandeira_do_Acre.svg.png'
    elif estado == 'RR':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Bandeira_de_Roraima.svg/140px-Bandeira_de_Roraima.svg.png'
    elif estado == 'RO':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Bandeira_de_Rond%C3%B4nia.svg/140px-Bandeira_de_Rond%C3%B4nia.svg.png'
    elif estado == 'AP':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Bandeira_do_Amap%C3%A1.svg/140px-Bandeira_do_Amap%C3%A1.svg.png'
    elif estado == 'PA':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Bandeira_do_Par%C3%A1.svg/140px-Bandeira_do_Par%C3%A1.svg.png'
    # Sul
    elif estado == 'SC':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Bandeira_de_Santa_Catarina.svg/140px-Bandeira_de_Santa_Catarina.svg.png'
    elif estado == 'RS':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Bandeira_do_Rio_Grande_do_Sul.svg/140px-Bandeira_do_Rio_Grande_do_Sul.svg.png'
    elif estado == 'PR':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Bandeira_do_Paran%C3%A1.svg/140px-Bandeira_do_Paran%C3%A1.svg.png'
        
def imagem_categoria(cat: str) -> str:
    """
        Recebe uma categoria como parâmetro e retorna a imagem correspondente desta.
        :param cat: String
    """
    if cat == 'Óbitos':
        return 'https://images2.imgbox.com/8b/ce/hYbjm1CM_o.png'
    elif cat == 'Casos':
        return 'https://images2.imgbox.com/31/23/vpnQTbju_o.png'
    else: # cat == "Vacinação"
        return 'https://images2.imgbox.com/c3/9e/cs7vxq1B_o.png'