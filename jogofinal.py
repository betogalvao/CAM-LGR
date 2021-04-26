import funcoesEP2 as ep2

print('Paciência Acordeão') 
print('==================')
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.')
print('Existem apenas dois movimentos possíveis: ')
print('1. Empilhar uma carta sobre a carta imediatamente anterior; ')
print('2. Empilhar uma carta sobre a terceira carta anterior. ')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: ')
print('1. As duas cartas possuem o mesmo valor ou ')
print('2. As duas cartas possuem o mesmo naipe. ') 
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. ')

input('Aperte [Enter] para iniciar o jogo...')

print('O estado atual do baralho é: ')
baralho = ep2.cria_baralho()
i = 1
for carta in baralho:
    print('{}. {}'.format(i,carta))
    i += 1

input_= int(input('Escolha uma carta (digite um número entre 1 e 52): '))
input_ -= 1

possivel = ep2.lista_movimentos_possiveis(baralho,input_)
if len(possivel) == 1:
    primeiro = possivel[0]
    ep2.empilha(baralho, input_, primeiro)
if len(possivel) == 2:
    qual = int(input('Sobre qual carta você quer empilhar o {}: 1. {} ou 2. {}? '.format(baralho[input_], baralho[input_ - 1], baralho[input_ - 3])))
    if qual == 1:
        ep2.empilha(baralho, input_, possivel[0])
    else:
        ep2.empilha(baralho, input_, possivel[1])

i2 = 1
for carta in baralho:
    print('{}. {}'.format(i2,carta))
    i2 += 1