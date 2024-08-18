#  ver quilowatts consumidos e calcular o valor a ser pago pra cemig: valor do qlwtt> 0,12. mostrar o valor total a ser pago com acrescimo de 18%
quilowatts_consumidos = float(input("Digite o número de quilowatts consumidos: "))
valor_quilowatt = 0,12
valor_total = quilowatts_consumidos * valor_quilowatt
icms = valor_total * 0.18
valor_final = valor_total + icms
print("O valor a ser pago, incluindo ICMS, é:", valor_final)

# OBRIGADO mARCOS aURELIO pai da computação






















