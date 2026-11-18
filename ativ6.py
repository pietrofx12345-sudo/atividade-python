Pulseira = input ("digite a cor que está na pulseira: ")

if Pulseira == "Verde":
    print("não urgente, atendimento em até 2 horas.")
elif Pulseira == "Amarelo":

    print("Urgente! atendimento em até 30 minutos.")
elif Pulseira == "Vermelho":
    print("Emergência! atendimento imediato!.")
else:
    print("Cor inválida, por favor,reavalie o paciente.")