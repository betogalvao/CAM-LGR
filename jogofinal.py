import funcoesEP2 as ep2

print('Paciência Acordeão') 
print('==================')
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. \n')
print('Existem apenas dois movimentos possíveis: ')
print('1. Empilhar uma carta sobre a carta imediatamente anterior; ')
print('2. Empilhar uma carta sobre a terceira carta anterior. \n')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: ')
print('1. As duas cartas possuem o mesmo valor ou ')
print('2. As duas cartas possuem o mesmo naipe. \n') 
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. \n')

input('Aperte [Enter] para iniciar o jogo...')

print('O estado atual do baralho é: ')
baralho = ep2.cria_baralho()
ep2.printdobaralho(baralho)

continuar = ep2.possui_movimentos_possiveis(baralho)

if continuar == True:
    while continuar:
        if len(baralho) == 1:
            print('\033[1;32;40mParabens, você ganhou!!!')
            jogardnv = input('\033[0;37;40mDeseja jogar de novo? (s/n) ')
            if jogardnv == 's':
                baralho = ep2.cria_baralho()
                ep2.printdobaralho(baralho)
            else:
                continuar = False
        elif len(baralho) != 1:
            continuar = ep2.possui_movimentos_possiveis(baralho)
            if continuar == False:
                print('\033[1;31;40mVocê perdeu')
                jogardnv = input('\033[0;37;40mDeseja jogar de novo? (s/n) ')
                if jogardnv == 's':
                    baralho = ep2.cria_baralho()
                    ep2.printdobaralho(baralho)
                    continuar = ep2.possui_movimentos_possiveis(baralho)
                else:
                    continuar = False
            else:
                input_= int(input('\033[0;37;40mEscolha uma carta (digite um número entre 1 e {}): '.format(len(baralho))))
                if input_ > len(baralho):
                    print('\033[1;31;40mPosição inválida ')
                else:
                    input_ -= 1
                    possivel = ep2.lista_movimentos_possiveis(baralho,input_)
                    if len(possivel) == 1:
                        primeiro = possivel[0]
                        ep2.empilha(baralho, input_, primeiro)
                        ep2.printdobaralho(baralho)
                    if len(possivel) == 2:
                        qual = int(input('\033[0;37;40mSobre qual carta você quer empilhar o {}: 1. {} ou 2. {}? '.format(baralho[input_], baralho[input_ - 1], baralho[input_ - 3])))
                        if qual == 1:
                            ep2.empilha(baralho, input_, possivel[0])
                            ep2.printdobaralho(baralho)
                        else:
                            ep2.empilha(baralho, input_, possivel[1])
                            ep2.printdobaralho(baralho)
                    if len(possivel) == 0:
                        print('\033[1;31;40mA carta {} não pode ser movida.'.format(baralho[input_]))