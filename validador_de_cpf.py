user_cpf = input('Valide seu CPF: ')

def calculo_cpf (digits, factor):
    total = 0
    for digit in digits:
        total += int(digit) * factor
        factor -= 1
    calculation = total * 10 % 11
    return 0 if calculation > 9 else calculation

first_digit = str(calculo_cpf(user_cpf[:9], 10))

second_digit = str(calculo_cpf(user_cpf[:10], 11))

cpf_gerado = f'{user_cpf[:9]}{first_digit}{second_digit}'

# print('CPF VÁLIDO' if cpf_gerado == user_cpf else 'CPF INVÁLIDO')
