#importando bibliotecas
import matplotlib.pyplot as plt
import random

#solicitando a quantidade de tiros
tiros = int(input('Quantidade de tiros: '))

#contador e listas que guardarão os pontos dentro/fora do disco x^2 + y^2 <= 1
cont = 0

listaxin = []
listayin = []
listaxout = []
listayout = []

#loop com geração de números aleatórios
for _ in range(tiros):
    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)

    c = (0,0)

    if (x - c[0])**2 + (y - c[1])**2 <= 1:
        listaxin.append(x)
        listayin.append(y)
        cont += 1
    else:
        listaxout.append(x)
        listayout.append(y)

print(4 * cont/tiros)

#Plotando o gráfico com os pontos que caíram dentro/fora do disco
plt.plot(listaxin, listayin,'o')
plt.plot(listaxout, listayout, 'o')
plt.title('Simulação de Monte Carlo')
plt.show()
