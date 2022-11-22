real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.35
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))

real = float(input('Quanto de dinheiro você tem na carteira? R$'))
euro = real / 5.51
print('Com R$ {:.2f} você pode comprar € {:.2f}'.format(real, euro))