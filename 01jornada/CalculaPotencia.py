N = input("Digite o número a ser potenciado: ")
N = int(N)

p = input("Digite a potência desejada: ")
p = int(p)

while((p < 0) or (N <= 1)):
    print("Entrada inválida")
    N = input("Digite o número a ser potenciado: ")
    N = int(N)
    p = input("Digite a potência desejada: ")
    p = int(p)

Potencia = 1
if p > 0:
    for j in range(1, p + 1):
        Potencia = Potencia * N

print()
print(N,"elevado a",p, ":",Potencia)
