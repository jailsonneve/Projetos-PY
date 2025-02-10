def calc(termosList, n):
    a1, a2 = termosList[0], termosList[1]
    r = a2 - a1
    resp = a1 + r * (n - 1)
    return resp

def soma_pa(termosList, n):
    a1, a2 = termosList[0], termosList[1]
    r = a2 - a1
    soma = (n / 2) * (2 * a1 + (n - 1) * r)
    return soma

def termo_pg(a1, r, n):
    return a1 * (r ** (n - 1))

def soma_pg(a1, r, n):
    if r == 1:
        return n * a1
    else:
        return a1 * (1 - r ** n) / (1 - r)

def menu():
    print();
    print("Escolha uma opção:")
    print("1 - Soma dos termos da P.A.")
    print("2 - Progressão aritmética (Tenha certeza que é realmente uma P.A.!)")
    print("3 - Progressão geométrica (Tenha certeza que é realmente uma P.G.!)")
    print("4 - Soma dos termos da P.G.")
    print("0 - Sair")
    print();
    opcao = int(input("Digite a opção: "))
    return opcao

def main():
    while True:
        opcao = menu()
        if opcao == 1:
            n = int(input("Digite o número de termos: "))
            termos = [float(i) for i in input("Digite os termos separados por espaço: ").split()]
            soma = soma_pa(termos, n)
            print(f"A soma dos {n} primeiros termos da progressão aritmética é {soma}")
        elif opcao == 2:
            n = int(input("Digite o número de termos: "))
            termos = [float(i) for i in input("Digite os termos separados por espaço: ").split()]
            if len(set(termos)) != n or termos[0] == termos[-1]:
                print("Esta não é uma progressão aritmética!")
                continue
            calculo = calc(termos, n)
            print(f"O {n}º termo da progressão aritmética é {calculo}")
        elif opcao == 3:
            n = int(input("Digite o número de termos: "))
            termos = [float(i) for i in input("Digite os termos separados por espaço: ").split()]
            a1 = termos[0]
            r = termos[1] / a1  # Razão calculada entre os dois primeiros termos
            # Verifica se a razão é constante entre os termos
            if all(termos[i] / termos[i - 1] == r for i in range(1, len(termos))):
                termo_n = termo_pg(a1, r, n)
                print(f"O {n}º termo da progressão geométrica é {termo_n}")
            else:
                print("Esta não é uma progressão geométrica!")
                continue
        elif opcao == 4:
            n = int(input("Digite o número de termos: "))
            termos = [float(i) for i in input("Digite os termos separados por espaço: ").split()]
            a1 = termos[0]
            r = termos[1] / a1
            soma = soma_pg(a1, r, n)
            print(f"A soma dos {n} primeiros termos da progressão geométrica é {soma}")
        elif opcao == 0:
            print("Saindo...")
            break

if __name__ == "__main__":
    main()