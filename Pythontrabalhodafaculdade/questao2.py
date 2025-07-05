#Menu
print('Olá, eu sou o Marcelo Augusto e seja Bem-vindo à MV Sorveteria & Açai')
print(23 * '-' + 'CARDAPIO' + 23 * '-')
print(54 * '-')
print(4 * '-' + ' | ' + ' Tamanho ' + ' | ' + ' Cupuaçu (CP) ' + ' | ' + ' Açaí (AC) ' + ' | ' + 4 * '-')
print(4 * '-' + ' | ' + '    P    ' + ' | ' + '  R$ 9.00     ' + ' | ' + ' R$ 11.00  ' + " | " + 4 *'-')
print(4 * '-' + ' | ' + '    M    ' + ' | ' + '  R$ 14.00    ' + ' | ' + ' R$ 16.00  ' + " | " + 4 *'-')
print(4 * '-' + ' | ' + '    G    ' + ' | ' + '  R$ 18.00    ' + ' | ' + ' R$ 20.00  ' + " | " + 4 *'-')
print(54 * '-')

valor = 0
continuar = True

#Definição de valor e tamanho do item comprado
while continuar:
    sabor = input('Digite o sabor que deseja (Cupuaçu (CP) ou Açaí (AC)): ')
    while sabor not in ["CP",'Cupuaçu' , "AC" , 'Açai']:
        print('Sabor Inválido. Tente Novamente!')
        sabor = input('Digite o sabor que deseja (Cupuaçu (CP) ou Açaí (AC)): ')

    tamanho = input('Digite o tamanho desejado: (P, M ou G): ')
    while tamanho not in ['P', 'M', 'G']:
        print('Tamanho Inválido. Tente Novamente!')
        tamanho = input('Digite o tamanho que deseja (P, M ou G): ')
    if sabor == 'CP':
        if tamanho == 'P':
            preco = 9.00
        elif tamanho == 'M':
            preco = 14.00
        elif tamanho == 'G':
            preco = 18.00

    elif sabor == 'AC':
        if tamanho == 'P':
            preco = 11.00
        elif tamanho == 'M':
            preco = 16.00
        elif tamanho == 'G':
            preco = 20.00
    valor += preco
    print(f'voce pediu um {sabor} de tamanho {tamanho}. O seu pedido deu no valor de {preco:.2f}.')

#Caso queira continuar
    deseja_pedir_algo_mais = input('Deseja pedir algo mais? (S/N):')
    while deseja_pedir_algo_mais not in ['S','N']:
        print('opção invalida. Deseja pedir algo mais? (S/N)')

#Caso não queira continuar
    if deseja_pedir_algo_mais == 'N':
        continuar = False

#Finalização da compra
print(f'O valor da sua compra ficou em R$ {valor:.2f}. Obrigado e volte sempre!')


