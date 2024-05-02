Nome = "luiz otavio"
idade= 40
peso= 95
altura=1.80
imc=peso/altura**2

linha_1= f"o nome dele é:{Nome}tem a idade de:{idade} a sua altura é de:{altura:.2f} e seu Imc é de:{imc:.3f} "

print(linha_1)




a= 1
b= 2
c= 3.1
string= "a={},b={},c={}"
formato= string.format(a,b,c)
print(formato)

a=1
b=2
c=3.1
print("a=",a ,"b=",b ,"c=",c)

a=1
b=2
c=3.10
linha_1=f"a={a},b={b},c={c:.2f}"
print(linha_1)

Nome= "luiz"
idade= 40
peso= 80
altura=1.70
imc=peso/altura**2

linha_1= f"o nome dele é:{Nome}, a sua idade é de:{idade} anos, tem o peso de:{peso} kg, a sua altura é:{altura:.2f} e tem o imc de:{imc:.3f}"
print(linha_1)


