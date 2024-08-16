lado1 = int(input('Quantos centímetros tem o primeiro lado do triângulo? '))
lado2 = int(input('Quantos centímetros tem o segundo lado do triângulo? '))
lado3 = int(input('Quantos centímetros tem o terceiro lado do triângulo? '))

if lado1 == lado2 == lado3:
    print('Triângulo Equilatero')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Triângulo Escaleno')
elif lado1 == lado2 or lado1 ==lado3:
    print('Triângulo Isósceles')
else:
    print('Não é um triângulo')