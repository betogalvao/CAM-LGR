def cria_baralho():
    import random
    numeros = ['A','A','A','A','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q','K','K','K','K']
    naipes = ['♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣', '♠', '♥', '♦', '♣']
    baralho = []

    contante = [0]*52

    for instante in contante:
        x = numeros[instante]
        y = naipes[instante]
        baralho.append(x + y)
        numeros.remove(x)
        naipes.remove(y)
        random.shuffle(baralho)
    return baralho

def extrai_naipe(carta):
    if '♦' in carta:
        return '♦'
    if '♥' in carta:
        return '♥'
    if '♣' in carta:
        return '♣'
    if '♠' in carta:
        return '♠'

def extrai_valor(carta):
    if 'A' in carta:
        return 'A'
    if '2' in carta:
        return '2'
    if '3' in carta:
        return '3'
    if '4' in carta:
        return '4'
    if '5' in carta:
        return '5'
    if '6' in carta:
        return '6'
    if '7' in carta:
        return '7'
    if '8' in carta:
        return '8'
    if '9' in carta:
        return '9'
    if '10' in carta:
        return '10'
    if 'J' in carta:
        return 'J'
    if 'Q' in carta:
        return 'Q'
    if 'K' in carta:
        return 'K'

def lista_movimentos_possiveis(baralho, input_):
    lista_possiveis = []
    if input_ == 0:
        return lista_possiveis
    else:
        if extrai_naipe(baralho[input_]) in baralho[input_ - 1] or extrai_valor(baralho[input_]) in baralho[input_ - 1]:
            lista_possiveis.append(1)
        if input_ < 3:
            return lista_possiveis
        else:
            if extrai_naipe(baralho[input_]) in baralho[input_ - 3] or extrai_valor(baralho[input_]) in baralho[input_ - 3]:
                lista_possiveis.append(3)
                return lista_possiveis
   
def empilha(baralho, input_, possiveis):
    baralho[possiveis] = baralho[input_]
    del(baralho[input_])
    return baralho

def possui_movimentos_possiveis(baralho):
    i = 1
    while i != len(baralho):
        while i < 3:
            if extrai_naipe(baralho[i]) in baralho[i - 1] or extrai_valor(baralho[i]) in baralho[i - 1]:
                return True
            else:
               i += 1
        while i >= 3:
            if extrai_naipe(baralho[i]) in baralho[i - 1] or extrai_valor(baralho[i]) in baralho[i - 1] or extrai_naipe(baralho[i]) in baralho[i - 3] or extrai_valor(baralho[i]) in baralho[i - 3]:
                return True
            else:
                i += 1
            if i == len(baralho):
                return False