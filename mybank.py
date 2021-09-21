print("------------------------------------")
print("    Seja bem vindo(a) ao My Bank    ")
print("      SIMULADOR DE EMPRÉSTIMO       ")
print("------------------------------------")

cliente = str(input("Você já é nosso cliente? s/n: "))

# definindo a taxa de juros dependendo do perfil do usuário.
if cliente == 'n':
    tarifa = 35
    score = int(input("Digite o seu Serasa Score: "))
    if score < 300:
        juros = 0.2
    elif score < 500:
        juros = 0.15
    elif score < 800:
        juros = 0.10
    elif score < 1000:
        juros = 0.05
    #print("Não é cliente")
else: 
    #print("É cliente do banco")
    tarifa = 0
    juros = 0.04

# solicitando as informações sobre o empréstimo
valor = float(input("Valor desejado para o empréstimo: "))
parcelas = int(input("Quantidade de parcelas: "))
seguro = str(input("Deseja incluir um seguro desemprego no seu empréstimo? s/n: "))

# cauculando os valores do empérestimo

valor_parcial = tarifa + valor + (valor * juros)
total = valor_parcial + (valor_parcial * 0.038)

if seguro == 's':
    total = total + (total * 0.035)
valor_parcelas = total / parcelas

print("Valor total: : ", total)
print("parcelas: ", valor_parcelas)
