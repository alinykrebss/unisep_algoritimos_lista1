#Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de
#conversão é: 𝑅 = 𝐺 ∗ 𝜋/180, sendo 𝐺 o ângulo em graus e 𝑅 em radianos e 𝜋 = 3.14.

###
# exercicio 14/46
# aluno: aliny krebs
# data 18/03/2024
####

ang_graus = float (input ("digite um angulo em graus  "))
ang_rad = float ( ang_graus  * 3.14 / 180) 
print (f" este angulo em radianos eh de: {ang_rad}")
