#Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida
#em m/s (metros por segundo). A fórmula de conversão é: 𝑀 =𝐾 3.6, sendo 𝐾 a velocidade em km/h e 𝑀 em m/s

###
# exercicio 10/46
# aluno: aliny krebs
# data 18/03/2024
####

velocodadeEmKmPorHora = float (input ("digite a velociade em Km/h "))
VelocidadeEmMPorSeg = float (  velocodadeEmKmPorHora / 3.6)
print (f"a velocidade em m/s eh de: {VelocidadeEmMPorSeg}")
