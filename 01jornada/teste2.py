""""
# 2.10-exercícios
2.1
.Vimos que n = 42 é legal. E 42 = n?
 erro de sintaxe e  não é possivel atribuir literal.

. x = y = 1?
 x e y tem valor 1.

 .Em algumas linguagens, cada instrução termina em um ponto e vírgula ;
 . O que acontece se você puser um ponto e vírgula no fim de uma instrução no Python?
 se for uma str, ela aparece sintax invalida, mas se for um int ou um float ela aparece normamente.

 .E se puser um ponto no fim de uma instrução?
 se for uma str da sintax inavalida,se for um int, ele vira um float e se for um float,da sintaxe invalida também.

 .Em notação matemática é possível multiplicar x e y desta forma: xy.
   O que acontece se você tentar fazer o mesmo no Python?
   da name error,senão colocar o sinal"*",não vai multiplicar.

   2.2
.O volume de uma esfera com raio r é 4/3 pi r ao cubo.
Qual é o volume de uma esfera com raio 5?
n=5*5*5
v=4*n/3
print(f"{v:.2f}")
166.67 pi

.Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%.
 O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional.
 Qual é o custo total de atacado para 60 cópias?

 n= 24.95 * 60
v=40*n/100
t=59*0.75 +3
print(v+t)

.Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), 
então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) 
e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?
k=60*8+15
k2=60*7+12
r=3*k2+2*k
r2=r/60
h=60*6+52
r3=r2+h
print(r3/60)

"""


