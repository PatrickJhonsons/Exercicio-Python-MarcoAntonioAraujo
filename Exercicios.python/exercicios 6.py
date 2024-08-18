# Calcular o salário líquido do funcionário sabendo que este é constituído pelo salário bruto mais o valor das horas extras subtraindo 8% de INSS do total. Serão lidos nesse problema o salário bruto, o valor das horas extras e o número de horas extras. Apresentar ao final o salário líquido.
salario_bruto = float(input("Digite o salário bruto: "))
valor_horas_extras = float(input("Digite o valor das horas extras: "))
num_horas_extras = int(input("Digite o número de horas extras: "))
total_horas_extras = valor_horas_extras * num_horas_extras
salario_total = salario_bruto + total_horas_extras
inss = salario_total * 0.08
salario_liquido = salario_total - inss
print("O salário líquido é:", salario_liquido)

# OBRIGADO mARCOS aURELIO pai da computação











