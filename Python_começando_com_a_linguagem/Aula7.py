# Formatação de saídas

print("R$ {:.2f}".format(1.5))
# R$ 1.50
print("R$ {:.2f}".format(1234.50))
# R$ 1234.50

print("Data {:02d}/{:02d}".format(9, 4))
# Data 09/04
print("Data {:02d}/{:02d}".format(19, 11))
# Data 19/11

print("R$ {:7.2f}".format(1234.50))
# R$ 1234.50
print("R$ {:7.2f}".format(1.5))
# R$    1.50

print("R$ {:07.2f}".format(1.5))
# R$ 0001.50