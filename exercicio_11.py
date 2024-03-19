#Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida emkm/h (quilômetros por hora).
# A fórmula de conversão é: 𝐾 = 𝑀 ∗ 3.6, sendo 𝐾 a
#velocidade em km/h e 𝑀 em m/s.

###
# exercicio 11/46
# aluno: aliny krebs
# data 18/03/2024
####

VelocidadeEmMPorSeg = float (input ("digite a velociade em m/s "))
velocodadeEmKmPorHora = float (  VelocidadeEmMPorSeg * 3.6)
print (f"a velocidade em km/h eh de: {velocodadeEmKmPorHora}")
