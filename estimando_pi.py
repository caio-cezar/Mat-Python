import numpy as np
import matplotlib.pyplot as plt
import random
import math

def monte_carlo(tiros):
        
    cont = 0

    for _ in range(tiros):
        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)

        c = (0,0)

        if (x - c[0])**2 + (y - c[1])**2 <= 1:
            cont += 1

    return 4 * cont/tiros
    
if __name__ == '__main__':  
    print(monte_carlo(1000))
    erro_absoluto = abs(monte_carlo(1000) - math.pi)
    erro_relativo = abs(((monte_carlo(1000) - math.pi ) / (math.pi)) * 100)
    print(f'Erro absoluto: {erro_absoluto}')
    print(f'Erro relativo(%): {erro_relativo:.2f}')
    


