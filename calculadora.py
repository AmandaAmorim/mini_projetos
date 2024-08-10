num1 = float(input('Digite o primeiro número: '))
num2 =  float(input('Digite o segundo número: '))
operacao = input('Qual operação deseja realizar? (+,-,*,/)')
# verifica escolha de operação
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 + num2
else:
    print('Operador inválido!')
    resultado = 0

if resultado % 1 == 0:
    print('o resultado é um número inteiro.')
else:
    print('o resultado é um número decimal.')
    
if resultado > 0: 
    print('O resultado é um número positivo.')
elif resultado == 0:
    print('O resultado é um número neutro.')
else:
    print('Oresultado é um número negativo')
    
if resultado % 2 == 0:
    print('O resultado é um número par.')
else:
    print('O resultado é um número ímpar.')    
   