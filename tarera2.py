import math

print("Selecione a atividade")
slc = int(input("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15:"))

def atividade(slc):
    match slc:
        case 1:
            #1 - Peça para o usuário digitar seu nome e exiba uma mensagem de boas-vindas. O
            #que é a entrada? O que é a saída?
                print("R: A entrada vai ser o nome da pessoa, E a saída será a mensagem de boas vindas com o nome da pessoa.")
                nome = str(input("Insira seu nome:"))
                print(f"Bem-vindo, {nome}!")

        case 2:
            #2 - Peça para o usuário digitar dois números com casa decimal, e exiba a soma.
            #Qual será a saída?
                print("EX: 2.5, 4.45, 3.14, ...")
                n1 = float(input("Insira um número decimal:"))
                n2 = float(input("Digite outro número decimal:"))
                print(n1 + n2)

        case 3:
            #3 - Receba dois números inteiros e uma operação (+, -, *, /) e exiba o resultado.
            #Dica: if, elif, else.
                n1 = int(input("Insira um número:"))
                n2 = int(input("Insira outro número:"))
                op = input("Selecione uma operação(+, -, *, /):")

                if op == "+":
                    print(n1 + n2);
                elif op == "-":
                    print(n1 - n2)
                elif op == "*":
                    print(n1 * n2)
                elif op == "/":
                    print(n1 / n2)
                else:
                    print(" Selecione uma operação válida!")

        case 4:
            #4 - Peça a idade do usuário em anos e exiba em meses e dias.
                idade = int(input("Quantos anos você tem?:"))
                print(f"Você tem {idade * 12} meses de vida")
                print(f"Você tem {idade * 365} dias de vida")

        case 5:
            #5 - Receba três notas e exiba a média do aluno. A nota será flutuante.
                n1 = float(input("Insira a primeira nota:"))
                n2 = float(input("Insira a segunda nota:"))
                n3 = float(input("Insira a terceira nota:"))
                print(f"Sua média é:{(n1 + n2 + n3) / 3}")

        case 6:
            #6 - Peça duas notas e calcule a média, informando se a média é suficiente para
            #aprovação (acima de 7).
                n1 = float(input("Insira a primeira nota:"))
                n2 = float(input("Insira a segunda nota:"))
                media = (n1 + n2) / 2 

                if media >= 7:
                    print("APROVADO")
                else:
                    print("REPROVADO")

        case 7:
            #7 - Peça o valor de um produto e o dinheiro pago. Exiba o troco.
                prod = float(input("Insira o valor do produto:$"))
                pago = float(input("Quanto você vai pagar:$"))
                troco = pago - prod
                if pago < prod:
                    print(f"Está faltando:${troco * -1}")
                else:
                    print(f"Seu troc é de:${troco}")

        case 8:
            #8 - Receba um valor em horas e exiba em minutos e segundos.
                hora = int(input("Insira um valor numérico:"))
                print(f"Esse valor corresponde a {hora * 60} minutos ou {hora * 3600} segundos")
                
        case 9:
            #9 - Peça o valor do lado de um quadrado e calcule o perímetro. No seu caso, qual
            #será a saída?
                print("RESPOSTA: A saída vai ser o perímetro do quadrado")
                lado = float(input("Insira o valor do lado quadrado:"))
                print(f"O perímetro do quadrado é {lado * 4}")
            
        case 10:
            #10 - Peça um número e calcule sua potência de 2.
                numero = float(input("Digite um número:"))
                print(f"A potência de {numero} é {numero * numero}")

        case 11:
            #11 - Peça um número e formate para inteiro. Informe se ele é positivo, negativo ou
            #zero. Dica: if, elif, else.
                numero = float(input("Digite qualquer número:"))
                formatado = round(numero)

                if formatado > 0:
                    print("O número é positivo.")
                elif formatado == 0:
                    print("O número é neutro")
                else:
                    print("O número é negativo")
            
        case 12:
            #12 - Peça a largura e o comprimento de um retângulo e calcule a área. Largura e
            #comprimento, nesse caso, serão números flutuantes.
            largura = float(input("Insira a largura"))
            comprimento = float(input("Insira o comprimento:"))
            area = largura * comprimento
            print(f"A área doo ret6angulo é {area}")

        case 13:
            #13 - Peça dois números inteiros e informe qual é o maior. Dica: if, elif, else.
            n1 = int(input("Insira um número:"))
            n2 = int(input("Insira outro número número:"))

            if n1 > n2:
                print(f"{n1} é o número maior.")
            elif n1 == n2:
                print("Os números são iguais")
            else:
                print(f"{n2} é o número maior.")
        case 14:
            #14 - Peça o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal
            peso = float(input("Digite seu peso:"))
            altura = float(input("Digite sua altura:"))
            imc = peso / (altura * altura)
            print(f"Seu IMC é {round(imc, 2)}")
        case 15:
            #15 - Peça a distância (flutuante) em quilômetros e a velocidade (flutuante) média de
            #um veículo. Calcule o tempo de viagem (em horas).
            distancia = float(input("Insira a distância:"))
            velocidade = float(input("Insira a valocidade média:"))
            viagem = distancia / velocidade;
            if viagem >=2:
                print(f"O tempo de viagem é de {round(viagem)} horas")
            elif viagem < 1:
                print(f"O tempo de viagem é de menos de uma hora")
            else:
                print(f"O tempo de viagem é de {math.floor(viagem)} hora")
        case _:
            print("Valor inválido")
atividade(slc)