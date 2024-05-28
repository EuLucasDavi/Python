# Função para converter data e hora em segundos
def converte_para_segundos(dia, hora, minuto, segundo):
    return dia * 86400 + hora * 3600 + minuto * 60 + segundo

# Função para converter segundos em dias, horas, minutos e segundos
def converte_de_segundos(segundos):
    dias = segundos // 86400
    segundos %= 86400
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return dias, horas, minutos, segundos

# Entrada
dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(' : '))
dia_fim = int(input().split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(' : '))

# Converte todos os tempos para segundos
inicio_em_segundos = converte_para_segundos(dia_inicio, hora_inicio, minuto_inicio, segundo_inicio)
fim_em_segundos = converte_para_segundos(dia_fim, hora_fim, minuto_fim, segundo_fim)

# Calcula a diferença em segundos
duracao_em_segundos = fim_em_segundos - inicio_em_segundos

# Converte a duração de segundos de volta para dias, horas, minutos e segundos
dias, horas, minutos, segundos = converte_de_segundos(duracao_em_segundos)

# Saída
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
