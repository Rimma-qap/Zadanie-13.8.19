def get_price(age):
    """Получение стоимости билета в зависимости от возраста"""

    if age < 18:
        return 0
    elif 18 <= age < 25:
        return 990
    return 1390


number_tickets = int(input('Введите количество билетов, которые хотите приобрести на конференцию: '))
ages = []

for number in range(number_tickets):
    age = int(input(f'Введите возраст посетителя №{number + 1}: '))
    ages.append(age)

full_price = sum(map(get_price, ages))
discount_price = int(full_price * 0.9)

if number_tickets > 3:
    print('Стоимость билетов со скидкой 10% составляет:', discount_price, 'руб.')
else:
    print('Стоимость билетов составляет:', full_price, 'руб.')
