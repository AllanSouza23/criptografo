# Fazer um programa que cifre uma frase de até 128 caracteres usando cifra de cesar
import os
from random import randint
from time import sleep

def caesar(frase, chave, modo):
    # Define aas possibilidades dentro do alfabeto
    alfabeto = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'
    nova_frase = ' ' 

    # Implementa um valor auxiliar para substituição de cada caractere
    aux = str(chave)
    aux = aux.split()
    n1 = int(aux[0][0])
    n2 = int(aux[0][1])
    n3 = int(aux[0][2])
    n4 = int(aux[0][3])
    soma = n1 + n2 + n3 + n4

    for letra in frase:
        # Encontra a localização original do caractere
        indice = alfabeto.find(letra)
        if indice == -1:
            # Se a letra não for encontrada
            nova_frase += letra
        else:
            # Encriptar cada letra encontrada
            novo_indice = indice + soma if modo == 1 else indice - soma
            novo_indice = novo_indice % len(alfabeto)
            nova_frase += alfabeto[novo_indice:novo_indice + 1]

    # Retorna a nova frase criada ao programa principal
    return nova_frase

def embaralhar(original, alterado):
    if alterado == True:
        # Separa cada palavra dentro da frase
        frase = original
        frase = frase.split(' ')
        
        # Organiza as palavras em ordem alfabetica
        frase.sort()

        # Concatena as palavras novamente dentro da frase
        frase = ' '.join(frase)

        # Retorno da frase embaralhada
        return frase
    else:
        # Retorna a frase original 
        return original

def compara_chave(chave, chave_digitada):
    # Define o número de tentativas e pede ao usuário a chave para comparação
    tentativas = 3
    chave_digitada = input(f'\nQual a chave de acesso?\nLembrando que você possui apenas {tentativas} tentativas!\n>>> ')

    for x in range(1, 4):
        # A cada vez que o usuário digita a chave para comparação, é subtraído 1 do valor de tentativas
        tentativas -= 1
        
        if chave_digitada.isnumeric():
            # Se a chave de comparação tiver valor numérico, é transformada em número inteiro e é comparada
            chave_digitada = int(chave_digitada)

            if (chave == chave_digitada):
                # Se for igual a chave de acesso, a mensagem original é apresentada
                print('Mensagem desencriptada: ', original)
                break

            elif (chave != chave_digitada and x != 3):
                # Se for diferente da chave de  acesso mas ainda houver tentativas, é perguntada novamente a chave de comparação
                print('A chave digitada possui valor incorreto')
                chave_digitada = input(f'\nQual a chave de acesso?\nLembrando que você possui apenas {tentativas} tentativa(s) restantes!\n>>> ')

        elif (not chave_digitada.isnumeric() and x != 3):
            # Se a chave digitada não for de valor numérico e ainda houverem tentativas, é solicitada uma nova chave de comparação
            print('A chave de acesso não possui letras ou espaços!')
            print(f'Você possui apenas {tentativas} tentativa(s) restantes!')
            chave_digitada = input('\nQual a chave de acesso?\n>>> ')

        if ((chave_digitada and x == 3) or (tentativas == 0)):
            # Se as tentativas se esgotarem o acesso é negado
            print('\nNúmero máximo de tentativas atingido.')
            sleep(1)
            print('\nAcesso negado!')
            break

def inicio(chave):
    # Gera um número aleatório para a operação, sendo ele entre 1000 e 9999
    chave = randint(1000, 9999)

    # Mensagens iniciais ao usuário
    print('\nOlá, bem vindo ao CriptoSeg, seu ambiente de mensagens protegidas por criptografia.')
    print('Meu nome é Poppy e serei seu guia e realizarei os processos do ambiente.')
    sleep(1)

    # Exibição da chave de acesso
    print(f'\nAqui está sua chave de acesso: {chave}')
    sleep(1)
    print('Lembre-se bem dela!')
    sleep(1.5)
    return chave
    
def reiniciar_programa():
    resposta = ' '
    while resposta != 'S' and resposta != 'N':
        # Verifica se o usuário deseja reiniciar o programa ou sair dele
        resposta = input('\nDeseja reiniciar o programa? \nDigite S para continuar ou N para sair: ')

        # Caso o usuário queira reiniciar o programa
        if resposta.upper() == 'S':
            # Isola a execução atual do programa para não haver confusão na execução futura
            print("\n" * os.get_terminal_size().lines)
            break

        # Caso o usuário opte por encerrar o programa
        elif resposta.upper() == 'N':
            # Saudação final
            print('Tudo certo, até a próxima!')
            sleep(2)
            exit(0)

# Início do programa principal
# Definições das variáveis iniciais
encripta = 1
embaralha = True
chave = 0
resposta = 'S'
chave_dig = ' '

while resposta == 'S':
    # Enquanto o usuário quiser executar o programa
    # Atribuição do valor da chave de acesso
    chave = inicio(chave)

    # Solicitação da frase a ser criptografada e verificação se ela possui de 1 até 128 caracteres
    original = input('Por favor, digite a mensagem que deve ser protegida: ')
    while ((len(original) > 128) or (len(original) < 1)):
        print('A mensagem deve ter no máximo 128 caracteres')
        original = input('Por favor, digite novamente a mensagem que deve ser protegida: ')    
    sleep(1)

    # Tratamento de criptografia para a frase 
    embaralhado = embaralhar(original, embaralha)
    cripto = caesar(embaralhado, chave, encripta)
    print('Mensagem encriptada: ', cripto)

    # Comparação para verificar se o usuário tem permissão para ver a mensagem
    compara_chave(chave, chave_dig)
    sleep(1)

    # Pergunta se o usuário que repetir o processo
    reiniciar_programa()
