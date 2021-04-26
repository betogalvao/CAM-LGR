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
for carta in ep2.cria_baralho():
    print('{}. {}'.format(i,carta))
    i += 1

input_= int(input('Escolha uma carta: '))
