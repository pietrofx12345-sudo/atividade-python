print("---SISTEMA DE AUDITORIA COMPLETO---")

for tentativa in range(3):
    #coletando e tratando os dados
    #remove o traço antes de checar o .isalnum() para a lógica funcionar
    codigo = input("Cód. relatório (Ex: REL101): ").strip().upper()
    data = input("Data (DD/MM/AAAA): ").strip()
    email = input("E-mail do auditor: ").strip().lower()
    id_auditor = input("ID numérico do auditor: ").strip()
    status = input("Status (digite APROVADO): ").strip().upper()

    #EXPLICAÇÂO DA LÓGICA:
    #o .isalnum() verifica se o codigo contem apenas letras e numeros (sem simbolos ou espaços)
    #o .count("/") == 2 garante que a data tem exatamente 2 barras, o que é essencial para o formato DD/MM/AAAA
    #o .count("@") 1 verifica se existe exatamente 1 arroba no email, o que é um requisito básico para um email válido
    #o .endswitch(".com")garante que o email termine corretamente.
    #o .isdigit() garante que o ID do auditor seja apenas numérico.
    if codigo.isalnum() and \
    data.count("/") == 2 and \
    email.count("@") == 1 and email.endswith(".com") and \
    id_auditor.isdigit() and \
    status == "APROVADO":

        print(f"\n SUCESSO: auditor (id_auditor), seu relatório {codigo} foi enviado! ")
        break
    else:
        print(f"\n ERRO: Dados inválidos! tentativa (tentativa = {tentativa + 1}) de 3. ")
        print("-" * 40)
else:
    print("\n SISTEMA BLOQUEADO. muitas falhas. procure o diretor de segurança. ")

#-------------------------------
# LEGENDA TÉCNICA: O QUE CADA FUNÇÃO FAZ NESTE CODIGO?
#--------------------------------

#1. .strip(): Remove espaços em branco no início e no final da string, garantindo que a validação não seja afetada por espaços acidentais.
#2. .upper(): Converte a string para letras maiúsculas, padronizando a entrada para facilitar a comparação, especialmente útil para campos como status ou códigos que devem ser case-insensitive.
#3. .lower(): Converte a string para letras minúsculas, útil para padronizar entradas como e-mails, onde a caixa alta ou baixa não deve afetar a validade.
#4. .isalnum(): Verifica se a string contém apenas caracteres alfanuméricos (letras e números), garantindo que o código do relatório não contenha caracteres especiais ou espaços.
#5. .count("/"): Conta quantas vezes o caractere "/" aparece na string, garantindo que a data esteja no formato correto (DD/MM/AAAA) com exatamente duas barras.,
#6. .endswith(".com"): Verifica se o e-mail termina com ".com", garantindo que o formato do e-mail seja válido.
#7. .isdigit(): Verifica se a string contém apenas dígitos, garantindo que o ID do auditor seja numérico.
#8 \ (ponte) : Usado para quebrar uma linha de código longa em várias linhas para melhorar a legibilidade, sem interromper a lógica do código.  
#9. (t + 1) : Exibe o número da tentativa atual, começando de 1 em vez de 0, para uma mensagem de erro mais amigável ao usuário.