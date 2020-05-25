def f(x):
    """
    Função em que será feita a aproximação da raíz no intervalo [a,b] usando o método da bisseção.
    """
    return x**3 - 6*x**2 + 3*x + 1

def bissec(inicio, fim, tol):
    """
    Método da bisseção com 3 parâmetros: início do intervalo, fim do intervalo e tolerância.
    """
    n = 1
    if f(inicio) * f(fim) > 0:
        return None
    elif f(inicio) * f(fim) == 0:
        if f(inicio) == 0:
            return inicio
        else:
            return fim
    else:
        xm = (inicio + fim)/2
        print(f'Iteração 1: {xm}')
        while abs(xm - inicio) > tol:
            if f(inicio) * f(xm) == 0:
                return xm
            elif f(xm) * f(fim) > 0:
                fim = xm
            else:
                inicio = xm
            xm = (inicio + fim)/2
            n += 1
            print(f'Iteração {n}: {xm}')
        return xm

if __name__ == "__main__":
    print(bissec(0,1,0.0001))
