print('Olá, seja Bem-vindo a Copiadora de Marcelo Augusto!')

def escolha_servico():
  while True:
    print('Escolha o serviço que deseja:')
    print('DIG - Digitalização')
    print('ICO - Impressão colorida')
    print('IPB - Impressão preto e branco')
    print('FOT - Fotocópia')

    servico = input('Digite o serviço desejado: ')

    if servico in 'DIG':
      print('Você escolheu Digitalização')
      return 1.10

    elif servico in 'ICO':
      print('Você escolheu Impressão colorida')
      return 1.00

    elif servico in 'IPB':
      print('Você escolheu Impressão preto e branco')
      return 0.40

    elif servico in 'FOT':
      print('Você escolheu Fotocópia')
      return 0.20

    else:
      print('Escolha inválida! Entra com o tipo de serviço novamente: DIG, ICO, IPB OU FOT.')

def num_pagina():
 while True:
      try:
          num_pagina = int(input('Digite o número de páginas que deseja:'))

          if num_pagina < 20:
           return num_pagina * 0 # Desconto de 0%

          if num_pagina >= 20 and num_pagina <= 200:
           return num_pagina * 15 # Desconto de 15%

          if num_pagina >= 200 and num_pagina <= 2000:
           return num_pagina * 20 # Desconto de 20%

          if num_pagina >= 2000 and num_pagina <= 20000:
           return num_pagina * 25 # Desconto de 25%

      except ValueError:
            print('Digite um número de páginas válido!')


def servico_extra():
  while True:
    print('Escolha o serviço extra na qual deseja:')
    print('1- Encadernação simples está (R$ 15.00)')
    print('2- Encadernação de capa dura está (R$ 40.00)')
    print('0- Caso não deseja mais nada, está (R$ 0.00')

    adicional = int(input('Digite o serviço extra desejado: '))
    if adicional == 1:
      return 15.00
    elif adicional == 2:
      return 40.00
    elif adicional == 0:
      return 0
    print('Escolha errada, tente novamente uma das opções: 1, 2 ou 0.')

def main():
  print('Vamos começar?')

  servico_preco = escolha_servico()
  num_pagina = num_pagina()
  servico_extra = servico_extra()

total = (servico_preco * num_pagina) + servico_extra


  print(f'Valor á ser pago foi de:')
  print(f'Serviço escolhido foi de: R${servico:2.f} por cada página')
  print(f'Número de página escolhido foi de: {int(num_paginas)}')
  print(f'Serviço extra escolhido foi de: R${servico_extra:.2f}')
  print(f'Total a ser pago foi de: R${total:2.f}')

  if __name__ == '__main__':
     main()
