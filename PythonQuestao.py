# O preço, ao consumidor, de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e com os impostos,
# ambos aplicados ao custo de fábrica. As porcentagens encontram-se na tabela a seguir. Faça um programa que receba o custo de 
# fábrica de um carro e mostre o preço ao consumidor.
# | CUSTO DE FÁBRICA                  | % DO DISTRIBUIDOR                    | % DOS IMPOSTOS                       |
# |-----------------------------------|--------------------------------------|--------------------------------------|
# | Até R$ 28.000,00                  | 5                                    | isento                               |
# | Entre R$ 28.000,01 e R$ 45.000,00 | 10                                   | 15                                   |
# | Acima de R$ 45.001,00             | 15                                   | 20                                   |

custodefabrica = float(input("Demonstre o valor de custo da fábrica: "))

if custodefabrica <= 28000:
	print("O preço do carro é: R$%.2f." % (custodefabrica + (custodefabrica * 0.05)))
elif custodefabrica <= 45000:
	print("O preço do carro é: R$%.2f." % (custodefabrica + (custodefabrica * 0.10) + (custodefabrica * 0.15)))
else:
	print("O preço do carro é: R$%.2f." % (custodefabrica + (custodefabrica * 0.15) + (custodefabrica * 0.20)))
