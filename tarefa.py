#1 - Crie uma variável chamada idade e atribua o valor 20 a ela. Em seguida, imprima
#o valor da variável. Qual é a saída (em tela) esperada após a execução do bloco de
#código? 

#R: A saída esperada é 20, pois a variável chamada recebeu o valor de 20

idade = 20;
print(idade);


#2 - Crie duas variáveis: nome e sobrenome. Atribua valores a elas e imprima o nome
#completo concatenado.

nome = "Wesley";
sobrenome = "Wolf";

print(f"{nome} {sobrenome}");

#3 - Crie uma variável numero e atribua o valor 10. Depois, imprima se o número é
#maior que 5. Qual tipo de dado é utilizado nessa questão?

#R: O tipo de dado utilizado é o dado numérico.

numero = 10;

if numero > 5:
    print("O número é maior que cinco.")
else:
    print("O número é menor que cinco")

#4 - Crie uma variável chamada peso e atribua um valor do tipo float (por exemplo,
#70.5). Imprima o valor da variável. Qual tipo de dado é utilizado nessa questão?

#R: O tipo de dado utilizado é do tipo float já que a variável peso possui um valor com parte decimal.

peso = 75.8;

print(peso)

#5 - Crie uma variável chamada cidade e atribua um valor do tipo string (por exemplo,
#"Guarapuava"). Imprima o valor da variável.

cidade = "Pitanga"
print(cidade)

#6 - Crie uma variável numero e atribua um valor a ela. Depois, use if-else para
#verificar se o número é positivo ou negativo.

numero1 = 49;

if numero1 > 0:
    print("O número é positivo");
elif numero1 == 0:
    print("O número é neutro");
else:
    print("O número é negativo");

#7 - Crie uma variável idade e atribua um valor a ela. Use if-else para verificar se a
#pessoa pode votar (idade maior ou igual a 16). Qual tipo de dado é utilizado nessa
#questão?

#R: O dado utilizado é do tipo numérico.abs

idadeVoto = 18;

if idadeVoto >= 16:
    print("Você pode voltar.")
else:
    print("Você não pode votar.")

#8 - Crie uma variável idade com o valor 15. Use uma condição if-else para verificar
#se a pessoa é maior ou menor de idade (considerando 18 anos como maioridade).
#Imprima "Maior de idade" ou "Menor de idade" conforme o caso.

idadeAdulto = 15;

if idadeAdulto >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#9 - Crie uma variável nota com o valor 7. Use uma estrutura if-else para verificar se
#a nota é maior ou igual a 5 (aprovação). Imprima "Aprovado" ou "Reprovado"

nota = 7;

if nota >= 5:
    print("Aprovado")
else:
    print("Reprovado")

#10 - Crie uma variável senha e atribua o valor "12345". Use uma condição if para
#verificar se a senha é igual a "12345" e imprima "Acesso permitido" se for verdade.
#Caso contrário, imprima "Acesso negado".

senha = int(input("Insira a senha:"));

if senha == (12345):
    print("Acesso permitido")
else:
    print("Acesso negado")

