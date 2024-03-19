#Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. 
#A fórmula de conversão é: 𝐶 = 𝐾 − 273.15, sendo 𝐶 a temperatura em Celsius e 𝐾 a
#temperatura em Kelvin.

###
# exercicio 8/46
# aluno: aliny krebs
# data 18/03/2024
####

temperaturaK= float (input ("digite a temperatura em kelvin  "))
converterC = float ( temperaturaK - 273.15)
print (f"a temperatura em graus  celsius eh de: {converterC}")
