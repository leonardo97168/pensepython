
def myfunc():
    print("ola,seja bem vindo")
def cumprimenta(nome):
    print("ola",nome)
def multiplica(x):
    return x*5
myfunc()
cumprimenta("gabriel")
cumprimenta("any")
print(multiplica(50))


def saudação(nome):
    return f"ola, {nome}"
print(saudação("jobson"))

def multiplicar(a,b):
    return a*b
print(multiplicar(3,2))

def mynomes(*nomes):
    for x in nomes:
        print(x)
mynomes("joão","leo")

def mynumers(numeros):
    for y in numeros:
        print(y)
number= [1,2,3,4,5,6,7,8,9]
mynumers(number)
mynumers(["peixe","carne"])

def repetir(n):
    for x in range(n):
        print(x)
repetir(3)      

listadeprodutos=["caneta","lapis","borracha"]
for x in listadeprodutos:
    print(x)

def myfunc(n):
    return lambda a: a*n
meuduplicador=myfunc(2)
print(meuduplicador(11))
meutriplicador=myfunc(3)
print(meutriplicador(11))


x= lambda a,b:a*b
print(x(2,5))

user= input ("digite o seu nome: " )
print("o seu nome é: ",user )

cars=["fusca","peugeot","chevette"]
x=cars[0]
print(x)
print(len(cars))



