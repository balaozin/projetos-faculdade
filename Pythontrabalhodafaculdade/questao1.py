print('Olá, eu sou Marcelo Augusto e seja Bem-vindo à loja de Compras & Vendas')

valor_unitario= float(input('Digite o valor do produto:'))
qtdeproduto= int(input('Digite a quantidade do produto que deseja:'))

valor_total= valor_unitario * qtdeproduto

if (valor_total * qtdeproduto < 2500): # O valor igual ou menor á 2500 o desconto será de 0%
 desconto = 0

elif (2500 >= valor_total * qtdeproduto < 6000): # O valor igual ou maior 2500 e menor que 6000 o desconto será de 4%
 desconto = 4

elif (6000 >= valor_total * qtdeproduto < 10000): # O igual ou maior á 6000 e menor que 10000 o desconto será de 7%
 desconto = 7

else:                        # O Valor igual ou maior que 10000 o desconto será de 11%
 desconto = 11

valor_total = valor_unitario * qtdeproduto
com_desconto = (valor_total * desconto / 100)

print('O valor sem desconto foi de: R$ {:.2f}'. format(valor_total))

print('O valor com o desconto foi de: {:.2f} (desconto {:.0f}%)'.format(valor_total - com_desconto, desconto))


