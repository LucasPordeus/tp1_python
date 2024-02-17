# Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.

minutos = int(input("Escolha uma quantidade de minutos: "))

def minutosParaHorasMinutos(quantidadeDeMinutos):
    horas = int(quantidadeDeMinutos / 60)
    minutosRestantes = quantidadeDeMinutos - (horas * 60)
    print("A quantidade de minutos ", quantidadeDeMinutos, "convertido para horas e minutos é ", horas, " horas e ", minutosRestantes, " minutos.")

minutosParaHorasMinutos(minutos)

print("Escolha uma quantidade de horas e em seguidas os minutos:")
horas = int(input("Horas: "))
minutosDeHoraMinutos = int(input("Minutos: "))

def horaMinutosParaMinutos(quantidadeDeHoras, quantidadeDeMinutos):
    horasEmMinutos = quantidadeDeHoras * 60
    horasMinutosEmMinutos = horasEmMinutos + quantidadeDeMinutos
    print("A quantidade de ", quantidadeDeHoras, " horas e ", quantidadeDeMinutos, " minutos convertidos em minutos são ", horasMinutosEmMinutos, " minutos.")

horaMinutosParaMinutos(horas, minutosDeHoraMinutos)