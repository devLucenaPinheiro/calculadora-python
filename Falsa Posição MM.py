# Metodo Falsa Posição
def falsaposicao(a,b,e):
    Nvezes = 1
    condicao = True
    while condicao:
        resul = a - (b-a) * f(a)/( f(b) - f(a) )
        print("Interação- %d, X= %0.6f e a função f(X)= %0.6f" % (Nvezes, resul, f(resul)))
        
        # Teorema de Bolzano
        if f(a) * f(resul) < 0:
            b = resul
        else:
            a = resul

        # Contador
        Nvezes = Nvezes + 1
        condicao = abs(f(resul)) > e

    print("\n A raiz aproximada e de: %0.8f" % resul)


# Input
f_string = input("Digite a função f(x): ")
f = eval('lambda x: ' + f_string)

a = float(input("Digite o primeiro chute: "))
b = float(input("Digite o segundo chute: "))
e = 1e-5

# Raiz
if f(a) * f(b) > 0:
    print("Os chutes não tem raiz. Tente de novo.")
else:
    falsaposicao(a,b,e)