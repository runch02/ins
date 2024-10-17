if __name__ == '__main__':
    P = 23
    G = 9
    print(f'The Value of P is: {P}')
    print(f'The Value of G is: {G}')
    
    a = 4
    print(f'Secret Number for Alice is: {a}')
    x = int(pow(G, a, P))
    
    b = 6
    print(f'Secret Number for Bob is: {b}')
    y = int(pow(G, b, P))
    
    ka = int(pow(y, a, P))
    kb = int(pow(x, b, P))
    
    print(f'Secret key for Alice is: {ka}')
    print(f'Secret key for Bob is: {kb}')
